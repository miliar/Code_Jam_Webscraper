/*
ID: reza_711
PROG: test
LANG: C++
*/
#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
 
 int main()
{
     ofstream fout("cgB.txt");
     ifstream fin("B.in");
     
	int n,j,k,l;
	fin>>n;
	int i=0;
	while(n>0)
	{
	    char str[1000],str1[1001];
		fin>>str;k=0;

		if(next_permutation(str,str+(strlen(str)))!=0)
        {     	i++;
		fout<<"Case #"<<i<<": "<<str<<endl;
     	}
		else 
        {  
              prev_permutation(str,str+strlen(str));
        strcat(str,"0");
            next_permutation(str,str+strlen(str)-k);
            l=0;
             while(str[l]=='0'){l++;}
             str[0]=str[l];
             str[l]='0';
             
             
             // k=strlen(str)-l;
             
             /*if(str[0]=='0')
             {
                            prev_permutation(str,str+strlen(str));
             	cout<<k<<": "<<str<<endl;
             l=strlen(str)-1;
             k=0;
             cout<<str[l]<<endl;
             while(str[l]=='0'){l--;k++;}
            
             next_permutation(str,str+strlen(str)-k);}
             
       //      next_permutation(str,str+strlen(str)-k);
//           //  strcat(str,"0");
             for( j=0;j<strlen(str);j++)
             {str1[j+1+k]=str[j];}
           /*  str1[j+1+k]='\0';
            while(k>0){ str1[k]='0';k--;}
             str1[0]=str[0];
             */
                  	i++;
		fout<<"Case #"<<i<<": "<<str<<endl;
	
             }
        
	    n--;
	}
   
     return 0;
}
