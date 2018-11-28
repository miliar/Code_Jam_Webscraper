#include<iostream>
#include<fstream>
#include<string.h>
#include<math.h>

using namespace std;

char sengine[100][150];
char squery[1000][150];
int pos;

int getMaxPool(int ne, int nq, int ini){
	int pose, posq, max = 0, am;
	for(pose = 0; pose < ne; ++pose){
		am = 0;
		for(posq = ini; posq < nq; ++posq){
			if(strstr(sengine[pose], squery[posq]) == NULL)
				am++;
			else
				break;
		}
		if(am > max){
			pos = pose;
			max = am;
		}
	}
	for(int b = ini; b < max; ++b)
		memset(squery[b], 0x45,150);
	//memset(sengine[pos], 0x45,150);
	return max;
}

int main(){
	char line[128];
	char resLine[128];
	int n, as, numq;

	ifstream fe("A-small-attempt1.in");
	ofstream fs("A-small-attempt1.ou");

	while(!fe.eof()){
		fe.getline(line,128);
		if(sscanf(line,"%i", &n) < 0)
			break;

		for(as = 0; as < n; ++as){
			fe.getline(line, 128);
			int nums, an;
			sscanf(line, "%i", &nums);
			for(an = 0; an < nums; ++an){
				fe.getline(line, 128);
				strcpy(sengine[an],line);
			}
			fe.getline(line, 128);
			sscanf(line, "%i", &numq);
			for(an = 0; an < numq; ++an){
				fe.getline(line, 128);
				strcpy(squery[an],line);
			}
			int sum = 0, sw = -1;
			while(sum < numq){
				sum += getMaxPool(nums, numq, sum);
				sw++;
			}
			if(sw == -1)
				sw=0;
			sprintf(resLine, "Case #%i: %i", as+1, sw);
			cout<<resLine<<endl;
			fs<<resLine<<endl;
		}

	}
	fe.close();
	fs.close();

	return 0;
}