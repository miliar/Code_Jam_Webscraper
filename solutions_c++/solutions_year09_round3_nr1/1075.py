#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

int main(int a, char **b)
{

       char ch,buff[61],old[20];
       int n,T, i,j,k,l;
	unsigned long mx,p;
	int lookup[36];	
       ifstream in(b[1]);

       if(!in){

               cout << "not present" << endl;
               return 0;
       }

 in >> T;
for (i=1; i<=T;i++){

		for(j=0;j<36;j++)
		lookup[j]=-1;


                //in.getline(buff, 50);
		in >> buff;
              //  strcpy(old,buff);
//              cout << buff << endl;
//                n=strlen(buff);
 //             cout << n << endl;


		
	
		for(j=0,k=0; buff[j] ; j++)
		{
			l = (buff[j]>='a'?buff[j]-'a':buff[j]-22);
			if (lookup[l] == -1){
				lookup[l] = k;
				buff[j] = k;
				k++;
			}else{

				buff[j]=lookup[l];
			}
		}	


		n = j;

		if(k == 1){
			k = 2;
		}

		for(j=0; j < n ; j++){
			if(buff[j] == 1 || buff[j] == 0)	buff[j] = 1-buff[j];
		}


	
		for(j=n-1,p=1,mx=0; j>=0 ; --j){
			mx += p*buff[j];
			p *= k; 
		}				




		cout << "Case #" << i << ": " << mx << endl;

	}
}
