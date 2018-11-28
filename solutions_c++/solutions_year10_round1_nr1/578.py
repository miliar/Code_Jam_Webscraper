#include <iostream>
#include <fstream>
using namespace std;

#define FOR(cont,to) for (int cont=0;cont<to;cont++)

int main(int argc, char *argv[]) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int cc;
	fin>>cc;
	char board[51][51];
	int place[51];
	for (int cn=0;cn<cc;cn++) {
		int n,k;
		fin>>n>>k;
		for (int i=0;i<n;i++) {
			place[i]=n-1;
			fin>>board[i];
		}
		
		for (int i=0;i<n;i++)
			for (int j=n-1;j>=0;j--) {
				if (board[i][j]!='.') {
					while (board[i][place[i]]!='.' && place[i]>j) place[i]--;
					swap(board[i][place[i]],board[i][j]);
				}
			}
		
//		for (int i=0;i<n;i++)
//			cout<<board[i]<<endl;
		
		bool r=false,b=false;
		
		for (int i=0;i<n;i++) {
			int count=1;
			for (int j=1;j<n;j++) {
				if (board[i][j-1]==board[i][j]) {
					if (board[i][j]!='.') {
						count++;
						if (count==k) {
							if (board[i][j]=='R') r=true;
							else b=true;
						}
					}
				} else count=1;
			}
		}
		
		for (int i=0;i<n;i++) {
			int count=1;
			for (int j=1;j<n;j++) {
				if (board[j-1][i]==board[j][i]) {
					if (board[j][i]!='.') {
						count++;
						if (count==k) {
							if (board[j][i]=='R') r=true;
							else b=true;
						}
					}
				} else count=1;
			}
		}
		
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				int count=1,l=1;
				while (i+l<n && j+l<n) {
					if (board[i+l-1][j+l-1]==board[i+l][j+l]) {
						if (board[i+l][j+l]!='.') {
							count++;
							if (count==k) {
								if (board[i+l][j+l]=='R') r=true;
								else b=true;
							}
						}
					} else count=1;
					l++;
				}
			}
		}
		
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				int count=1,l=1;
				while (i-l>=0 && j+l<n) {
					if (board[i-l+1][j+l-1]==board[i-l][j+l]) {
						if (board[i-l][j+l]!='.') {
							count++;
							if (count==k) {
								if (board[i-l][j+l]=='R') r=true;
								else b=true;
							}
						}
					} else count=1;
					l++;
				}
			}
		}
		
		
		if (b&&r)
			fout<<"Case #"<<cn+1<<": Both"<<endl;
		else if (b)
			fout<<"Case #"<<cn+1<<": Blue"<<endl;
		else if (r)
			fout<<"Case #"<<cn+1<<": Red"<<endl;
		else
			fout<<"Case #"<<cn+1<<": Neither"<<endl;
	}
	fout.close();
	fin.close();
}
