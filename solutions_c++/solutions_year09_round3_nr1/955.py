#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string.h>
#include <set>
#include <stdio.h>
#include <stdlib.h>
#include <set>

using namespace std;


int compare (const void * a, const void * b)
{
    return ( *(char*)a - *(char*)b );
}



class Map {
public:
    void parse(istream& inn) {
        long int L;
        inn>>L;
        char tab[255];
        char tab2[255];
        for (int i=1;i<=L;i++) {
        //	for (int i=1;i<=1;i++) {
            memset(tab,-1,255);
            //memset(tab2,0,255);
            string s;
            inn>>s;
            char * mes=(char*) s.c_str();
            int size=s.length();
            cout<<"Case #"<<i<<": ";
            int x=1;
			//cout<<"size "<<size<<endl;
            for (int i=0;i<size;i++) {
                if (tab[mes[i]]==-1) {
					//cout<<"i "<<i<<endl;
                    tab[mes[i]]=x;
                    if (x==1) {x=0;continue;};
                    if (x==0) {x=2;continue;};
					x++;
                }
            }
			if ((x==0) || (x==1)) x=2;
			//cout<<"x "<<x<<endl;
            int base=1;
            long int res=0;
            for(int i=size-1;i>=0;i--){
			  res+=base*tab[mes[i]];
			  base*=x;
			}
			cout<<res<<endl;
        };
}

};

int main(int argc,char** argv) {
    Map map;
    //ifstream myfile("in.txt");
    //map.parse(myfile);
    map.parse(cin);
}

