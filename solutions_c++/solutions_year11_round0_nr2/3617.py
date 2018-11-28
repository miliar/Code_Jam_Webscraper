#include <iostream>
#include <cstdio>
//#include <cstring>

using namespace std;

struct combinedElements{
	char one, two, res;
};

struct opposedElements{
	char one, two;
};

combinedElements ceList[36];
opposedElements oeList[28];

int cn, dn, nn, rn;
char invokeList[100];
char result[100];

int findCombinedPair(char a, char b){
	int i;
	for (i=0; i<cn; i++)
		if (((a==ceList[i].one)&&(b==ceList[i].two)) || ((a==ceList[i].two)&&(b==ceList[i].one)))
			return i;
	return -1;
}

bool findOpposedPair(char a, char b){
	int i;
	for (i=0; i<dn; i++)
		if (((a==oeList[i].one)&&(b==oeList[i].two)) || ((a==oeList[i].two)&&(b==oeList[i].one)))
			return true;
	return false;
}

int main(){
	int tc;
	int i,j,k;
	char buffer[10];
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tc;
	for (i=0; i<tc; i++){
		cin >> cn;
		for (j=0; j<cn; j++){
			cin >> buffer;
			ceList[j].one = buffer[0];
			ceList[j].two = buffer[1];
			ceList[j].res = buffer[2];
		}

		cin >> dn;
		for (j=0; j<dn; j++){
			cin >> buffer;
			oeList[j].one = buffer[0];
			oeList[j].two = buffer[1];
		}

		cin >> nn;
		cin >> invokeList;

		rn = 0;
		for (j=0; j<nn; j++){
			if (rn==0)
				result[rn++] = invokeList[j];
			else{
				int d = findCombinedPair(invokeList[j], result[rn-1]);
				if (d!=-1)
					result[rn-1] = ceList[d].res;
				else{
					for (k=0; k<rn; k++)
						if (findOpposedPair(invokeList[j], result[k])){
							rn=0;
							break;
						}
					if (rn!=0)
						result[rn++] = invokeList[j];
				}
				
				/*else if (findOpposedPair(invokeList[j], result[rn-1])){
					rn = 0;
				}else
					result[rn++] = invokeList[j];*/
			}
		}

		cout << "Case #" << i+1 << ": [";
		for (j=0; j<rn; j++){
			cout << result[j];
			if (j!=rn-1)
				cout << ", ";
		}
		cout << "]\n";
	}
	return 0;
}