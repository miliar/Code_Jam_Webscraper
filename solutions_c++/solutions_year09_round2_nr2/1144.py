#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string.h>
#include <set>
#include <stdio.h>
#include <stdlib.h>

using namespace std;


int compare (const void * a, const void * b)
{
    return ( *(char*)a - *(char*)b );
}




class Map {
public:
    void parse(istream& inn) {
        long int L;
        long int i;
        inn>>L;
        string s;
        int poz,j;
        char max;
        char* number;
        for (int i=1;i<=L;i++) {
		//for (i=1;i<=1;i++) {
			//if (i<2) continue;
            inn>>s;
            poz=-1;
            number=(char*)s.c_str();
            max=0;
            cout<<"Case #"<<i<<": ";
            int rozmiar=s.length();
            for (j=rozmiar-1;j>=0;j--) {
                if (number[j]>=max) max=number[j];
                else {
                    poz=j;
                    break;
                }
            }
			//cout<<"j"<<j<<endl;
            char tmp;
			int k;
            if (j>=0) {
                tmp=number[j];
				k=rozmiar-1;
				while(number[k]<=tmp){
				  k--;
				}
                number[j]=number[k];
                number[k]=tmp;
                //sortowanie
                qsort(&number[j+1],rozmiar-(j+1),sizeof(char),compare);

                for (j=0;j<rozmiar;j++) {
                    cout<<number[j];
                }
            }
		  else {
			k=rozmiar-1;
			while(number[k]=='0'){
			  k--;
			  if (k<0) break;
			};
			if (k>=0){
			  tmp=number[k];
			  number[k]=number[rozmiar-1];
			  number[rozmiar-1]=tmp;
			}
            for (j=rozmiar-1;j>=0;j--) {
                if (j==rozmiar-2) cout<<'0';
                cout<<number[j];
            }
			if (rozmiar==1) cout<<'0';
            //dorabiania 0 gdzien na poczatku a wczesniej sortowanie
        }
        cout<<endl;
    }

}
};

int main(int argc,char** argv) {
    Map map;
    //ifstream myfile("B-small-attempt1.in");
    //map.parse(myfile);
    map.parse(cin);
}

