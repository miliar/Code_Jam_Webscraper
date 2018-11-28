#include <cstdlib>
#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    ifstream filein("/home/rohit/codejam/A-small-attempt1.in");
    ofstream fileop("/home/rohit/codejam/A-small-attempt1.out");
    char c;
   char map[27];
    char input[150]= "qzejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv****";
    char output[150]="zqourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup****";
    for(int i=0;i<26;i++)map[i]='#';
    map[26]='\0';
    //cout<<input[10];
     for(int i=0;input[i]!='*';i++)map[input[i]-'a']=output[i];
    int notc;
    
    filein>>notc;
    cout<<notc<<endl;
     string str;
    getline(filein,str);
    //sscanf(str,"%d",&notc);
    for(int i=1;filein.good()&&i<=notc;i++){
             
        getline(filein,str);
        //cout<<str;
        fileop<<"Case #"<<i<<": ";
     for(int j=0;j<str.size();j++){
     if(str[j]==' ')fileop<<' ';
     else fileop<<map[str[j]-'a'];
     }
    fileop<<endl;
    
    }
    filein.close();
    fileop.close();
    
    return 0;
}

