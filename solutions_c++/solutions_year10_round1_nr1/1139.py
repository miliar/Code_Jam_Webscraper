#include <iostream>
#include <string>
#include <vector>

using namespace std;

string getColor(vector <string> board, int K){
	int sz = board.size(),bcount = 0,rcount = 0;
	bool b = false, r = false;
 	for	(int i=0;i<sz ;i++){
 		for(int j=0;j<sz ;j++){
			
 		     bcount = rcount =0;
	 		 for(int x = i; x < i+K && x < sz; x++){
	 		 	if(board[x][j] == 'R')
	 		 		rcount++;
	 		 	else if(board[x][j] == 'B')
	 		 		bcount++;
	 		 }
	 		 if(bcount == K)
	 		 	b = true;
	 		 if(rcount == K)
	 		 	r = true;
	 		 	
 			bcount = rcount =0;
			for(int y = j; y < j+K && y < sz ; y++){
				if(board[i][y] == 'R')
	 		 		rcount++;
	 		 	else  if(board[i][y] == 'B')
	 		 		bcount++;
			}
	 		 if(bcount == K)
	 		 	b = true;
	 		 if(rcount == K)
	 		 	r = true;
	 		 	
 			bcount = rcount =0;
			for(int x = i,y = j; x < i+K && y < j+K && x < sz && y < sz ; x++, y++){
				if(board[x][y] == 'R')
	 		 		rcount++;
	 		 	else  if(board[x][y] == 'B')
	 		 		bcount++;
			}
	 		 if(bcount == K)
	 		 	b = true;
	 		 if(rcount == K)
	 		 	r = true;

 			bcount = rcount =0;
			for(int x = i+K-1, y = j; x >= i &&  x >=0 && y < j+K && x < sz && y < sz ; x--, y++){
				if(board[x][y] == 'R')
	 		 		rcount++;
	 		 	else  if(board[x][y] == 'B')
	 		 		bcount++;
			}
	 		 if(bcount == K)
	 		 	b = true;
	 		 if(rcount == K)
	 		 	r = true;

 		}
 	}

	if(b && r)
		return "Both";
	if(b)
		return "Blue";
	if(r)
		return "Red"; 		 
	return "Neither";
}

int main(){
	int T, N,K;
	string str;
	char temp;
	cin >> T;
	for(int i=0;i< T;i++){
		cin >> N >> K;
		getline(cin,str);
		vector <string> board;
		for(int j=0;j< N;j++){
			getline(cin,str);
			string tempstr (N,'.');
			int index = N-1;
			for(int k = N -1 ; k >= 0 ; k--){
				if(str[k] != '.'){
					tempstr[index--] = str[k];
				}
			}
			board.push_back(tempstr);
		}
		cout << "Case #"<< i+1 << ": " << getColor(board,K)<<endl;
	}
	return 0;
}
