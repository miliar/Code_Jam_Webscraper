#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string.h>

using namespace std;
char pos[300];
void makeglobal() {
    for (int x=0;x<300;x++) pos[x]=0;
    pos['w']=1;
    pos['l']=3;
    pos['t']=9;
    pos['d']=14;
    pos['j']=17;
    pos['a']=18;
}

void getposition (char letter,vector<char>& lista) {
    char z;
    if (z=pos[letter]) {
        lista.push_back(z);
        return;
    }
    if (letter=='e') {
        lista.push_back(2);
        lista.push_back(7);
        lista.push_back(15);
        return;
    }

    if (letter=='c') {
        lista.push_back(4);
        lista.push_back(12);
        return;
    }

    if (letter=='o') {
        lista.push_back(5);
        lista.push_back(10);
        lista.push_back(13);
        return;
    }

    if (letter=='m') {
        lista.push_back(6);
        lista.push_back(19);
        return;
    }

    if (letter==' ') {
        lista.push_back(8);
        lista.push_back(11);
		lista.push_back(16);
        return;
    }
    return;
};

class Data {
public:
    long datas[20];
    Data() {
        for (int y=1;y<20;y++) datas[y]=0;
        datas[0]=1;
    };
    Data(const Data& d2) {
        memcpy(this->datas,d2.datas,20*sizeof(long));
    }
    Data& operator= (const Data& d2) {
        memcpy(this->datas,d2.datas,20*sizeof(long));
        return *this;
    }

};

class Parse {
public:
    int l;
	long dddd[20];
    
    void parse() {
        //ifstream f("data.txt");
        //f>>l;
		cin>>l;
        //cout<<l<<endl;
        string line;
        getline(cin,line);
        //for (int x=0;x<l;x++) {
        for (int x=0;x<l;x++) {
            getline(cin,line);
            //cout<<line<<endl;
            int size=line.length();
            char position;
            char c;
			for(int x=1;x<20;x++) dddd[x]=0;
			dddd[0]=1;
            for (int x=0;x<size;x++) {
                //for(int x=0;x<size/3;x++){
                c=line.c_str()[x];
             //   cout<<"---"<<c<<endl;
                vector<char> tmp;
                getposition(c,tmp);
				for (vector< char >::iterator z=tmp.begin();z!=tmp.end();z++){
				  position=(*z);
				  if (dddd[position-1]) dddd[position]+=dddd[position-1];
				}
			     for(int x=0;x<20;x++){
				//	cout<<dddd[x]<<" ";
				  }
			
				//cout<<endl;
			}
			cout<<"Case #"<<x+1<<": "<<setfill ('0')<<setw(4)<<dddd[19]%1000<<endl;
        };
    };

};


int main(int argc,char** argv)
{
    makeglobal();
    Parse p;
    p.parse();
}

