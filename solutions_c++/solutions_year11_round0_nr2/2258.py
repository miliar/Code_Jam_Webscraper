#include <string>
#include <iostream>
#include <list>
#include <map>
#include <algorithm>
#include <math.h>

using namespace std;
void  output(int , int );
string s;
 map <string, char> form;
 map <char, string> oppose;
int main() 
{
    //--------------------------------
    int  t;
    cin >> t;
    int  _case = 1;
	for(;_case<=t;_case++)
	{     
       int C,D,N;
       
       cin >> C;
       string str;
       while(C-->0)
       {    cin >> s;      
            form[s.substr(0,2)] = s[2]; 
            char ch = s[1]; s[1]=s[0]; s[0] = ch;      
            form[s.substr(0,2)] = s[2];         
       }
       cin >>  D;
       while(D-->0)
       {  cin >> s; 
          oppose[s[0]].append(s.substr(1,1));
          oppose[s[1]].append(s.substr(0,1)); 
       }
       cin >> N;        cin >> s;            
       string out = "";
       //-----------
       output(0,N);
       for(int i=0; i<N; i++)
          if(s[i]!='_') out = out + s[i];
       //cout << s << endl;   
       //------------- o/p --------------
	   cout << "Case #" << _case << ": [" ;
	   if(out.length() > 0)
	   {
	   for(int i=0; i<out.length()-1; i++)
    	   {
              cout << out[i] << ", " ;
           }
           cout << out[out.length()-1] ; }
	   cout << "]" << endl;
	   form.clear();
	   oppose.clear();
	}
	return 0;
}

void output(int i, int n)
{
       if(i >= n) return;
       //cout << "@ ----  i= " << i << ", n= " << n<< endl;
       for(; i<n; i++)
       {
          //cout << "checking " << i << ", with string = "<< s << " and small string = " << s.substr(i,2) <<  endl;
          if ( form.count(s.substr(i,2)) > 0)
          {
            s[i] = form[s.substr(i,2)];
            s[i+1] = '_';
            i++;
          }
          else if (oppose.count(s[i]) > 0)
          {
              int j;
              //cout << "dwa : " << oppose[s[i]]  << " | " <<  s[i] << endl;   
              for(j=i+1; j<n; j++ )
              {
                if(oppose[s[i]].find(s[j]) !=string::npos )
                {   
                  //cout << j << ", yeah " << endl  ;
                  output(i+1,j);                   
                  if(oppose[s[i]].find(s[j]) !=string::npos )
                  {
                        //cout << "found "<< "i= " << i <<", j= " << j  << endl;
                        i = j;            
                        while(j >= 0)    
                        {  s[j]='_';   j--; }
                        //i = k;
                        break;                     
                  }
                }  
              }  
          }   
       }      
    return;         
}       

