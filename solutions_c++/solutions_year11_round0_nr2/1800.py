#include <iostream>
#include <fstream>

using namespace std;

fstream in("in.txt", fstream::in);
fstream out("out.txt", fstream::out);

typedef char triple [3];

void SolveCase(int casen){
	int C, D, N, (*douseen)[2];
	char (*tri)[4], (*dou)[3], *que, *res;
	in >> C;
	tri = new char [C] [4];
	for(int i = 0; i < C; i++) in >> tri[i];
	in >> D;
	dou = new char [D] [3];
	douseen = new int [D] [2];
	for(int i = 0; i < D; i++){
		in >> dou[i];
		douseen[i][0] = 0;
		douseen[i][1] = 0;
	}
	in >> N;
	que = new char [N + 1];
	res = new char [N + 1];
	in >> que;
	int posQ = 0, posR = 0;
	while(posQ < N){
		res[posR] = que[posQ];
		// Combination
		if(posR > 0){
			bool combined = false;
			int posC = 0;
			while(!combined && (posC < C)){
				if(((res[posR] == tri[posC][0]) && (res[posR - 1] == tri[posC][1]))
					|| ((res[posR] == tri[posC][1]) && (res[posR - 1] == tri[posC][0]))){
						posR--;
						// Should remove the element from the seen list, if it is presented there
						for(int posD = 0; posD < D; posD++){
							if			(res[posR] == dou[posD][0]) douseen[posD][0]--;
							else if (res[posR] == dou[posD][1]) douseen[posD][1]--;
						}
						res[posR] = tri[posC][2]; combined = true;
				}
				posC++;
			}
		}
		// Oposition
		for(int posD = 0; posD < D; posD++){
			if(((douseen[posD][0] > 0) && (res[posR] == dou[posD][1]))
				|| ((douseen[posD][1] > 0) && (res[posR] == dou[posD][0]))){
					// Clean the list
					posR = -1;
					for(posD = 0; posD < D; posD++){
						douseen[posD][0] = 0;
						douseen[posD][1] = 0;
					}
			}
			else if(res[posR] == dou[posD][0]) douseen[posD][0]++;
			else if(res[posR] == dou[posD][1]) douseen[posD][1]++;
		}
		posR++; posQ++;
	}
	// Outputting the result
	out << "Case #" << casen << ": [";
	for(int i = 0; i < posR - 1; i++)
		out << res[i] << ", ";
	if(posR > 0) out << res[posR - 1];
	out << "]" << endl;
	delete[] tri;
	delete[] dou;
	delete[] que;
	delete[] res;
}

int main(){
	int T; in >> T;
	for(int t = 0; t < T; t++)
		SolveCase(t + 1);
	return 0;
}
