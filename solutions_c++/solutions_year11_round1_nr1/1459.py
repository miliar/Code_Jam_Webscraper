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

class FreeCell{
public:
	void start(vector< vector<int> > &c ){
		int i,num;
		stringstream out(stringstream::in | stringstream::out);
		
		for(i=0;i<c.size();i++){
            if(getSeq(c[i]))
    		  out << "Case #" << (i+1) << ": "<< "Possible" << endl;
    		else
    		  out << "Case #" << (i+1) << ": "<< "Broken" << endl;
        }
		cout << out.str();
	}
	bool getSeq( vector<int> c){
        int i;
        if(c[1] <  100 && c[2] == 100)  return false;
        else if(c[1] > 0 && c[2] == 0)  return false;
        if(c[0] > 100)  c[0] = 100;
        for (i=1;i<= c[0];i++)
            if(isInteger((double)i * c[1] / 100)  )
                return true;
        return false;
    }
    bool isInteger(double a){   return floor(a) == a;}
};


 void getContent(vector< vector< int > > &c){
    int i,j,cases, numC;
	scanf("%d\n", &cases);
	numC = 3;
	for(i=0;i<cases;i++){
        //scanf("%d\n", &numC);
        vector<int> task;
        int tmp;
        for(j=0;j<numC;j++){
            scanf("%d", &tmp);
            task.push_back(tmp);
        }
        scanf("\n");
        c.push_back(task);    
    }
}
    
void print(vector< vector<int> >c){
     int i,j;   
     for(i=0;i<c.size();i++){
        for(j=0;j<c[i].size();j++)
            cout << c[i][j] << " ";
        cout << endl;
    }
}
  
int main(int argc, char *argv[]){
	vector< vector< int > > c;

	getContent(c);

	//print(c);
	//GoroSort *cs = new GoroSort();
	FreeCell *fc = new FreeCell();
	
	fc->start(c);
	return 0;
	//string out = bt->getTime(v);
}
