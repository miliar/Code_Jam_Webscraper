#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

long int times;
string welcome="welcome to code jam";

int search (string str,int j,int i){
    while (str[j]!='\0'){
        if (welcome[i]==str[j]){
            if (welcome [i+1]=='\0')times++;
            search (str,j+1,i);
            i++;
        }
        j++;
    }
    
    return 0;
}

int main(int argc, char *argv[])
{
    int n=0,i=0;

    fstream f("data.in",ios::in);
    fstream f2("data.out",ios::out);
    char char_str[500];
    string str;


    f>>n;
    cout<<n<<"\n";
    f.getline(char_str,500,'\n');
    

//!!!!
    for (i=0;i<n;i++){
        f.getline(char_str,500,'\n');
        str=char_str;
        times=0;
        search(str,0,0);
        if (times/10==0)f2<<"Case #"<<i+1<<": 000"<<times<<"\n";
        else if (times/100==0)f2<<"Case #"<<i+1<<": 00"<<times<<"\n";
        else if (times/1000==0)f2<<"Case #"<<i+1<<": 0"<<times<<"\n";
        else f2<<"Case #"<<i+1<<": "<<times%10000<<"\n";
        
    }  
    f2.close();
    f.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
