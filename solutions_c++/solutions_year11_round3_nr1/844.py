#include<stdio.h>
#include<iostream>
#include<sstream>
#include<vector>
#include<math.h>
#include<set>
#include<map>
#include<algorithm>
//#include<pair>

using namespace std;

class Ruby{
public:
	void start(vector< vector< string > > &c ){
		int i,j;
		stringstream out(stringstream::in | stringstream::out);

		for(i=0;i<c.size();i++){
    		out << "Case #" << (i+1) << ":" << endl;
                //cout << endl << "getting " << j <<".."<<endl ;
                if(!getSeq(c[i]))  out << "Impossible" << endl;
                else{
                    for(j=0;j<c[i].size();j++)
                        out << c[i][j] <<endl;
                }
        }
		cout << out.str();
	}
	bool getSeq( vector< string > &c){
        int i,j;
        for(i=0;i<c.size();i++)
            for(j=0;j<c[0].size();j++){
                //cout << "getSeq: i ,j = " <<i <<", " << j<<endl;
                if( c[i][j] == '#')
                    if(!toRuby(c,i,j))
                        return false;
        }
        return true;
    }       
    bool toRuby(vector< string > &c, int x, int y){  
        int i,j;
        //cout <<"toRuby: x, y= " << x << ", " << y <<endl;
        if(x == c.size()-1 || y == c[0].size()-1) return false;
        for(i=0;i<2;i++)
            for(j=0;j<2;j++)
                if(c[x+i][y+j] != '#')  return false;
        c[x][y] = '/'; c[x+1][y] = '\\'; c[x][y+1] = '\\';  c[x+1][y+1] = '/';
        //printS(c);
        return true;
    }
    void printS(vector< string > &c){
        int i;
        //cout << "printS:"<<endl;
        for(i=0;i<c.size();i++)
            cout << c[i]<<endl;
    }
  
};


 void getContent(vector< vector<string> > &c){
    int i,j,k,cases, row,col;
	scanf("%d\n", &cases);
	for(i=0;i<cases;i++){
        scanf("%d %d\n", &row, &col);
        vector<string> task;
        char tmp[51];
        memset(tmp, '\0', sizeof(tmp));
        for(j=0;j<row;j++){
            scanf("%s\n", tmp);
            task.push_back( string(tmp) );
        }
        c.push_back(task);    
    }
}

void print(vector< vector<string> >c){
     int i,j;   
     for(i=0;i<c.size();i++){
        for(j=0;j<c[i].size();j++)
            cout << c[i][j] << " ";
        cout << endl;
    }
}
  
int main(int argc, char *argv[]){
	vector< vector< string > > c;
    //cout <<"in main"<<endl;
	getContent(c);
    //print(c);
	//print(c);
	Ruby *cs = new Ruby();
	cs->start(c);
	return 0;
	//string out = bt->getTime(v);
}
