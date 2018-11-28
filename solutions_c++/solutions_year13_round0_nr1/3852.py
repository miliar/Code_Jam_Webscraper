#include <iostream>
#include <cstdio>

using namespace std;

class TicTacToe{
   
   int table[4][4]; 
   public:
   TicTacToe() {}
   
   void SetTable(){
      int n = 1;
      int i = 0;
      int j = 0;
      char val;
      for ( i = 0; i <= 3; i++ ){
         for ( j = 0; j <= 3; j++ ){
			cin >> val;
			if (val=='X')
            	table[i][j] = 10; 
            else if (val=='O')
            	table[i][j] = 1;
            else if (val=='T')
            	table[i][j] = 2;
            else table[i][j] = 0;
            n++;
         }
      }
   } 
   
   
  
   int CheckWinner(){
	  for(int i = 0; i <= 3; i++){
         if(!(table[i][0]==0 || table[i][1]==0 || table[i][2]==0 || table[i][3]==0)){
         	int val = table[i][0]*table[i][1]*table[i][2]*table[i][3];
			 if(val==2 || val==1){
				cout <<"O won\n";	
				return 1;
			 }else if(val==10000 || val==2000){
				cout <<"X won\n";
				return 1;
			 }
		 }
      }
      for(int i = 0; i <= 3; i++){
         if(!(table[0][i]==0 || table[1][i]==0 || table[2][i]==0 || table[3][i]==0)){
			int val = table[0][i]*table[1][i]*table[2][i]*table[3][i];
         	if(val==2 || val==1){
				cout <<"O won\n";	
				return 1;
			 }else if(val==10000 || val==2000){
				cout <<"X won\n";
				return 1;
			 }
		}
      }
      if(!(table[0][0]==0 || table[1][1]==0 || table[2][2]==0 || table[3][3]==0)){
	      	int val = table[0][0]*table[1][1]*table[2][2]*table[3][3];
	 		
			 if(val==1 || val==2){
				cout <<"O won\n";
				return 1;
			}else if(val==10000 || val==2000){
				cout <<"X won\n";
				return 1;			
			}       	 
	 }
		
	if(!(table[0][3]==0 || table[1][2]==0 || table[2][1]==0 || table[3][0]==0)){
	    int val = table[0][3]*table[1][2]*table[2][1]*table[3][0];
		if(val==1 || val==2){
			cout <<"O won\n";
			return 1;
		}else if(val==10000 || val==2000){
			cout <<"X won\n";
			return 1;			
		}
 
	}
	
	return 0;
   } 
   void CheckDraw(){
      int n = 1;
      int i = 0;
      int j = 0;
      int counter = 0;
        
      for( i = 0; i <= 3; i++ ){
         for( j = 0; j <= 3; j++ ){
			if(table[i][j] !=0){ 
               counter++; 
            }
            n++;
         }
      }
      if( counter ==16) 
      {
         cout << "Draw\n";
      }else cout <<"Game has not completed\n";
     
   }
};
 
int main(){
	
	freopen("A-large.in","r",stdin);
	freopen("out_a.txt","w",stdout);
	int t;
	cin>>t;
	bool done = false, GameOver = false;
	char Player = 'O', num;
	TicTacToe myGame;
	myGame.SetTable();
	
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		if(!myGame.CheckWinner())
			myGame.CheckDraw();
		myGame.SetTable(); 	
	}


	
	return 0;
}


