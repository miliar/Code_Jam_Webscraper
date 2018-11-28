#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <conio.h>
#include <string>
#include <climits>

using namespace std;

#define dv(vectName) for(int ii=0;ii<vectName.size();ii++) cout<<vectName[ii]<<' '; cout<<endl;
#define d1da(arrayName,size) for(int ii=0;ii<size;ii++) cout<<arrayName[ii]<<' '; cout<<endl;
#define d2da(arryName,row,col) for(int ii=0;ii<row;ii++){ for(int jj=0;jj<col;jj++) cout<<arryName[ii][jj]<<' '; cout<<endl; } cout<<endl; 

#define miii map<int,int>::iterator
#define mici map<int,char>::iterator
#define mcii map<char,int>::iterator
#define vii vector<int>::iteartor

#define pb(vectName,value) vectName.push_back(value);
#define mi(mapName,keyType,valType,key,val) mapName.insert(pair<keyType,valType>(key,val));



//fstream inp("c-small.in",ios::in);
//fstream inp("c-small1.in",ios::in);
//fstream out("c-small.out",ios::out);
fstream inp("c-large.in",ios::in);
fstream out("c-large.out",ios::out);
//fstream out("c-small1.out",ios::out);



string mother="welcome to code jam";
const char chars[11]={'w','e','l','c','o','m',' ','t','d','j','a'};
const int nods=11; 
map<string,int> pm;
map<int,string> mp;

int work[19][500];

bool present(char c){
     bool answer=false;
     for(int i=0;i<nods;i++){
             if(chars[i]==c){
                             answer=true;
                             break;
             }
     }
     return answer;
}







string strip(string text){
       string answer="";
       for(int i=0;i<text.length();i++){
               if(present(text[i])) answer+=text[i];
       }
       return answer;
}
       


void solve(int testCaseNo){
     char input[500];
     memset(input,'\0',500*sizeof(char));
     inp.getline(input,501);
     string text(input);          
     //text=strip(text);
     //cout<<text<<endl;
     memset(work,0,sizeof(int)*500*19);
     int R=mother.length(),C=text.length();
     for(int i=C-1;i>=0;i--){
             work[18][i]=work[18][i+1];
             if(text[i]=='m') work[18][i]++;
     }
     for(int i=0;i<18;i++) work[i][C-1]=0;
     for(int c=C-2;c>=0;c--)
             for(int r=17;r>=0;r--){
                     work[r][c]=work[r][c+1];
                     if(text[c]==mp[r][0]) work[r][c]=(work[r][c]%10000+work[r+1][c+1]%10000)%10000;
                     //if(text[c]==mp[r][0]) work[r][c]=(work[r][c]+work[r+1][c+1]);
             }
     int answer = work[0][0];
     string sanswer(4,'0');
     for(int i=3;i>=0;i--){
                   sanswer[i]='0'+answer%10;
                   answer/=10;
     }
                    
     out<<"Case #"<<testCaseNo<<": "<<sanswer<<endl;
     //cout<<"Case #"<<testCaseNo<<": "<<sanswer<<endl;
     /*cout<<"Info "<<endl;
     cout<<"work[18][] = "<<work[mother.length()-1][text.length()-3];*/
     
             
     
     //cout<<text<<endl;     
     //cout<<endl;
}



int main(void){     
    for(int i=0;i<mother.length();i++){
            string partial(mother,i);            
            pm.insert(pair<string,int>(partial,i));
            mp.insert(pair<int,string>(i,partial));
            //cout<<partial<<endl;
    }    
    int N;
    cin>>N;            
    for(int i=1;i<=N;i++)
            solve(i);
    getch();
    return 0;
}


/*int main(void){
    FILE* inp;
    fstream("c-small.out",ios::out);
    
*/
