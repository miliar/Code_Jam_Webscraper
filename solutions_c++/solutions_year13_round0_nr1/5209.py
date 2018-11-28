#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

char calculation (int x, int o, int t ){
     
     if (x==3 && t==1 ) return 'X';
     if (x==4 ) return 'X';
     if (o==3 && t==1 ) return 'O';
     if (o==4 ) return 'O';
     return 'D';
};

void getData (char character[16], int a, int b, int c, int d, int& x, int& o, int& t, int& space ){
     switch (character[a]) {
                case 'X' : x++;
                break;
                case 'O': o++;
                break;
                case 'T': t++;
                break;
                default: space++;
                break;
                }
     switch (character[b]) {
                case 'X' : x++;
                break;
                case 'O': o++;
                break;
                case 'T': t++;
                break;
                default: space++;
                break;
                }
     switch (character[c]) {
                case 'X' : x++;
                break;
                case 'O': o++;
                break;
                case 'T': t++;
                break;
                default: space++;
                break;
                }
     switch (character[d]) {
                case 'X' : x++;
                break;
                case 'O': o++;
                break;
                case 'T': t++;
                break;
                default: space++;
                break;
                }
          
}



int main()
{
	int case_num = 0;
	int i,j,k,p,q,total_space,x,o,t,space =0;

	
  
	string result,s = "";
	char character[16];
    char status ='D';

	cin >> case_num; getline (cin, s);
	//cout << "case_num is " << case_num << endl;
	//cout << "First s is " << s << endl;


	for (i = 0; i < case_num; i++) {

	
		for (k = 0;k< 4; k++) {
		    getline (cin, s);
		//cout << "s is " << s << endl;
		//cout << "s.length is " << s.length() << endl;

               for (j = 0; j < s.length(); j++) {
			       if (s[j] != ' ') 
				      character[k*4+j]= s[j];
                
			    }//end of j loop
       }//end of k loop
      
      getline (cin, s);
      
      //Display the character array conent
      //cout << "************************************"<< endl;
      //for (p = 0;p< 4; p++) {
      //    for (q = 0;q< 4; q++) {
      //        cout<< character[p*4+q];
      //    }
      //    cout <<endl;
      //}
      //cout << "************************************"<< endl;
      
      total_space=0;
      status ='D';
      
      x=o=t=space=0;
      getData(character,0,1,2,3,x,o,t,space);
      status = calculation(x,o,t);
      total_space = total_space + space;
     
      
      if (status =='D'){
         x=o=t=space=0;
         getData(character,4,5,6,7,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
         
      }
      
      if (status =='D'){
         x=o=t=space=0;
         getData(character,8,9,10,11,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
         
      }
      
      if (status =='D'){
         x=o=t=space=0;
         getData(character,12,13,14,15,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
      }
      if (status =='D'){
         x=o=t=space=0;
         getData(character,0,4,8,12,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
         
      }
      if (status =='D'){
         x=o=t=space=0;
         getData(character,1,5,9,13,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
         
      }
      if (status =='D'){
         x=o=t=space=0;
         getData(character,2,6,10,14,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
        
      }
      if (status =='D'){
         x=o=t=space=0;
         getData(character,3,7,11,15,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
         
      }
      if (status =='D'){
         x=o=t=space=0;
         getData(character,0,5,10,15,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
         }
      if (status =='D'){
         x=o=t=space=0;
         getData(character,3,6,9,12,x,o,t,space);
         status = calculation(x,o,t);
         total_space = total_space + space;
      }
      
      if (status =='D' && total_space !=0 ) status='N' ;
        
      switch (status) {
                case 'X' : result = "X won";
                break;
                case 'O': result = "O won";
                break;
                case 'D': result = "Draw";
                break;
                case 'N': result = "Game has not completed";
                break;
                default: result="Error";
                break;
                }
    
        


		cout << "Case #" << i + 1 << ": " << result << endl;
	}//end of case_num loop
}

