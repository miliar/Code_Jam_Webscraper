#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string go_throught(string in){
    string ans="";
    ans.resize(in.size());
    for(int i=0;i<in.length();i++){
        if(in[i]=='a'){ans[i]='y';}
        if(in[i]=='b'){ans[i]='h';}
        if(in[i]=='c'){ans[i]='e';}
        if(in[i]=='d'){ans[i]='s';}
        if(in[i]=='e'){ans[i]='o';}
        if(in[i]=='f'){ans[i]='c';}
        if(in[i]=='g'){ans[i]='v';}
        if(in[i]=='h'){ans[i]='x';}
        if(in[i]=='i'){ans[i]='d';}
        if(in[i]=='j'){ans[i]='u';}
        if(in[i]=='k'){ans[i]='i';}
        if(in[i]=='l'){ans[i]='g';}
        if(in[i]=='m'){ans[i]='l';}
        if(in[i]=='n'){ans[i]='b';}
        if(in[i]=='o'){ans[i]='k';}
        if(in[i]=='p'){ans[i]='r';}
        if(in[i]=='q'){ans[i]='z';}
        if(in[i]=='r'){ans[i]='t';}
        if(in[i]=='s'){ans[i]='n';}
        if(in[i]=='t'){ans[i]='w';}
        if(in[i]=='u'){ans[i]='j';}
        if(in[i]=='v'){ans[i]='p';}
        if(in[i]=='w'){ans[i]='f';}
        if(in[i]=='x'){ans[i]='m';}
        if(in[i]=='y'){ans[i]='a';}
        if(in[i]=='z'){ans[i]='q';}
        if(in[i]==' '){ans[i]=' ';}
    }
    return ans;
}

int main()
{
    int N;
    ifstream ifile;
    ifile.open("input.txt");
    ifile>>N;
    ofstream ofile;
    ofile.open("output.txt");
    string in;
    getline(ifile,in);
    for(int y=0;y<N;y++){
        getline(ifile,in);
        ofile<<"Case #"<<y+1<<": "<<go_throught(in)<<endl;
    }
    return 0;
}
