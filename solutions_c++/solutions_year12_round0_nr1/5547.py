#include <fstream>
#include <cstring>
using namespace std;
int main()
{
    char xs[30]="yhesocvxduiglbkrztnwjpfmaq";
    int num,i,j;
    ifstream myfile("A-small-attempt3.in");
    ofstream outfile("2.txt");
    myfile>>num;
    
    char G[105];
    myfile.getline(G,105);
    char chnG[105];
    for(i=1;i<=num;i++)
    {
       chnG[0]='\0';
       myfile.getline(G,105);
       for(j=0;j<strlen(G);j++)
          if (G[j]!=' ') chnG[j]=char(xs[G[j]-97]);
          else chnG[j]=' ';
       chnG[j]='\0';
       outfile<<"Case #"<<i<<": "<<chnG<<endl;       
    }
    return 0;
}
