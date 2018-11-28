//#include <stdlib>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("C.in" , "r" , stdin);
    freopen("C.out" , "w" , stdout);
    
    int T;   
    cin>>T;
    

     for(int caseID = 1 ; caseID <= T ; caseID ++){
		// vector<int> allCandy;
		 int num;
		 cin >> num;
		 int countByPatrick=0;
		 int leastCandy=0;
		 int allCandy=0;

		 for(int i = 0 ; i < num ; i ++){
			 int candy;
			 cin >> candy;
			 allCandy += candy;
			 if(leastCandy == 0){
				 leastCandy = candy;
			 }else  if(candy < leastCandy)
				 leastCandy = candy;

			 //allCandy.push_back(candy);
			 int temp_rst=0; int square =1;

			 do 
			 {
				 if( (countByPatrick %2) != (candy %2) ) {
					 temp_rst += square;					 
				 }
				 square = 2*square;
				
				 countByPatrick = countByPatrick >>1;
				 candy = candy >> 1;

			 } while (countByPatrick && candy);

			 if(countByPatrick){
				 temp_rst += square* countByPatrick;
			 }else{
				 temp_rst += square* candy;
			 }
			
			 countByPatrick = temp_rst;

		 }
		
		 if(!countByPatrick){
			cout<<"Case #"<<caseID<<": "<<(allCandy-leastCandy)<<endl;
		 }else{
			cout<<"Case #"<<caseID<<": NO"<<endl;
		 }


     }
     

   // system("PAUSE");
    return 0;
}
