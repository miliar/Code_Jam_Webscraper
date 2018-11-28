#include<iostream>
#include<fstream>
#include<cstring>
#include <map>

using namespace std;

int main (){
    map<char,char> gmap;
    
    gmap.insert ( pair<char,int>('a','y') );
    gmap.insert ( pair<char,int>('b','h') );
    gmap.insert ( pair<char,int>('c','e') );
    gmap.insert ( pair<char,int>('d','s') );
    gmap.insert ( pair<char,int>('e','o') );
    gmap.insert ( pair<char,int>('f','c') );
    gmap.insert ( pair<char,int>('g','v') );
    gmap.insert ( pair<char,int>('h','x') );
    gmap.insert ( pair<char,int>('i','d') );
    gmap.insert ( pair<char,int>('j','u') );
    gmap.insert ( pair<char,int>('k','i') );
    gmap.insert ( pair<char,int>('l','g') );
    gmap.insert ( pair<char,int>('m','l') );
    gmap.insert ( pair<char,int>('n','b') );
    gmap.insert ( pair<char,int>('o','k') );
    gmap.insert ( pair<char,int>('p','r') );
    gmap.insert ( pair<char,int>('q','z') );
    gmap.insert ( pair<char,int>('r','t') );
    gmap.insert ( pair<char,int>('s','n') );
    gmap.insert ( pair<char,int>('t','w') );
    gmap.insert ( pair<char,int>('u','j') );
    gmap.insert ( pair<char,int>('v','p') );
    gmap.insert ( pair<char,int>('w','f') );
    gmap.insert ( pair<char,int>('x','m') );
    gmap.insert ( pair<char,int>('y','a') );
    gmap.insert ( pair<char,int>('z','q') );
    gmap.insert ( pair<char,int>('\0','\0') );
    gmap.insert ( pair<char,int>(' ',' ') );

    fstream inputFile,outFile;
    inputFile.open("small1.in");
    outFile.open("small.out");
    if(inputFile.fail()){
        cout<<"Fail to open the File"<<endl;
    } 
    int T;
    scanf("%d",&T);
    int count =1;
    while(T>0){
        char *array = new char [102];
        char inp;
        inputFile.getline(array, 102, '\n');
        for(int i=0;i<strlen(array);i++){
            char inp;
            inp= gmap[array[i]];
            array[i] = inp;
        }    
        cout<<"Case #"<<count<<": "<<array<<endl;
        count++;
        delete array;
        T--;    
    }
    inputFile.close();
    outFile.close();
    return 0;
}    
                
