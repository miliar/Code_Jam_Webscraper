
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <deque>
#include <stack>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <set>
#include <map>
#include <numeric>
#include <ctime>
#include <functional>
#include <queue>

using namespace std;

void map_str(const string &source,string &dest)
{
     int i,n=source.size();
     dest=source;
     for (i=0;i<n;i++)
     {
         switch (source[i])
         {
                case 'y':dest[i]='a';break;
                case 'n':dest[i]='b';break;
                case 'f':dest[i]='c';break;
                case 'i':dest[i]='d';break;
                case 'c':dest[i]='e';break;
                case 'w':dest[i]='f';break;
                case 'l':dest[i]='g';break;
                case 'b':dest[i]='h';break;
                case 'k':dest[i]='i';break;
                case 'u':dest[i]='j';break;
                case 'o':dest[i]='k';break;
                case 'm':dest[i]='l';break;
                case 'x':dest[i]='m';break;
                case 's':dest[i]='n';break;
                case 'e':dest[i]='o';break;
                case 'v':dest[i]='p';break; 
                case 'z':dest[i]='q';break;
                case 'p':dest[i]='r';break;
                case 'd':dest[i]='s';break;
                case 'r':dest[i]='t';break;
                case 'j':dest[i]='u';break;
                case 'g':dest[i]='v';break;
                case 't':dest[i]='w';break;
                case 'h':dest[i]='x';break;
                case 'a':dest[i]='y';break;
                case 'q':dest[i]='z';break;
                default:dest[i]=source[i];
         }
     }
     
}
int main()
{
    FILE *f;
    int t=0;
    int i=0,j;
    char s[100],c;
    string s1,str[30],ans[30];
    f=fopen("ans.txt","w");
    ifstream is;
    //fscanf(f,"%d",t);
    //fclose(f);
    //cout<<"hey";
    is.open("A-small-attempt1.in");
    getline(is,s1);
    cout<<s1<<endl;
    while (i<s1.size())
    {t*=10;t+=s1[i]-48;i++;}
    
    cout<<t<<endl;
    for (i=0;i<t;i++)
    {
        getline(is,str[i]);
        //str[i]=s;
        cout<<str[i]<<endl;
    }
    for (i=0;i<t;i++)
    {
        map_str(str[i],ans[i]);
        cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
        fprintf(f,"Case #%d: ",i+1);
        for (j=0;j<ans[i].size();j++)
            fprintf(f,"%c",ans[i][j]);
        fprintf(f,"\n");
    }
      fclose(f);     
     is.close();  
    system("pause");
    return 0;
}
