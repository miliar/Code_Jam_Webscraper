#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

char botSeq[100];
int butSeq[100];
vector<int> oSeq;
vector<int> bSeq;
int oPos, bPos, oSeqPos, bSeqPos, n;
int timeTaken;
bool oActed, bActed;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tc;
	int i,j;

	cin >> tc;

	for (i=0; i<tc; i++){
		oPos = 0;
		bPos = 0;
		oSeqPos = 0;
		bSeqPos = 0;
		oSeq.clear();
		bSeq.clear();
		timeTaken = 0;

		cin >> n;
		for (j=0; j<n; j++){
			cin >> botSeq[j];
			cin >> butSeq[j];
			
			if (botSeq[j] == 'O')
				oSeq.push_back(butSeq[j]);
			else
				bSeq.push_back(butSeq[j]);
		}

		for (j=0; j<n;){
			oActed = bActed = false;

			if (!oSeq.empty())
			if ((oPos != oSeq[oSeqPos]) && (!oActed)){
				if (oPos < oSeq[oSeqPos])
					oPos++;
				else 
					oPos--;
				oActed = true;
			}


			if (!bSeq.empty())
			if ((bPos != bSeq[bSeqPos]) && (!bActed)){
				if (bPos < bSeq[bSeqPos])
					bPos++;
				else 
					bPos--;
				bActed = true;
			}
			
			if ((botSeq[j]=='O') && (!oActed)){
				if (oPos == butSeq[j]){
					if (oSeqPos<oSeq.size()-1)
						oSeqPos++;
					j++;
					oActed = true;
				}
			}else if ((botSeq[j]=='B') && (!bActed)){
				if (bPos == butSeq[j]){
					if (bSeqPos<bSeq.size()-1)
						bSeqPos++;
					j++;
					bActed = true;
				}
			}

			timeTaken++;

		}

		cout << "Case #" << i+1 << ": " << timeTaken-1 << endl;

	}
	

	cin >> tc;
}