//created by chairdog
//08052010

#include <iostream>
#include <fstream>
using namespace std;

struct Node{
	long num;
	Node * Next;
};

int main(){
	char iFile[30], oFile[30];
	cout << "dataset: ";
	cin.getline(iFile,30);
	ifstream inf(iFile);
	cout << "outfile: ";
	cin.getline(oFile,30);
	ofstream outf(oFile);

	int T;
	inf >> T;
	for (int counter=1; counter <= T; counter++){
		long R,K;
		int N;
		inf >> R >> K >> N;
		Node *G=new Node;
		Node *Head=G;
		for (int i=0; i < N; i++){
			inf >> G->num;
			G->Next= new Node;
			G=G->Next;
			G->Next=NULL;
		}
		G = Head;
		if (N>=2){
			while (G->Next->Next!=NULL) G=G->Next;
			delete G->Next;
			G->Next=Head;
		}
		else{
			delete G->Next;
			G->Next=Head;
		}

		long Seat=K, y=0;
		while (R > 0){
			Seat=K;
			R--;
			int group=0;
			while (Seat-Head->num >= 0 && group <N){
				Seat-=Head->num;
				Head = Head->Next;
				group++;
			}
			y+=K-Seat;
		}

		outf << "Case #" << counter << ": " << y << endl;
		cout << "Case #" << counter << ": " << y << endl;
		y=0;
		if (N>=2){
			G=Head->Next;
			Head->Next = NULL;
			while(G!=NULL){
				Head = G->Next;
				delete G;
				G=Head;
			}
		}
		else{
			delete Head;
			G=NULL;
		}
	}
	inf.close();
	outf.close();
	return 0;
}
