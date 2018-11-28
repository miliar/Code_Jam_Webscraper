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

class RPI{
public:
    double cache[100][100];
	void start(vector< vector< string > > &c ){
		int i,j;
		stringstream out(stringstream::in | stringstream::out);
		
		for(i=0;i<100;i++)
		  for(j=0;j<100;j++)
		      cache[i][j] = -10;
		for(i=0;i<c.size();i++){
    		out << "Case #" << (i+1) << ":" << endl;
    		//cout << "case " << i<< "..." <<endl;
            for(j=0;j<c[i].size();j++){
                //cout << endl << "getting " << j <<".."<<endl ;
                out << getSeq(c[i], j) << endl;
            }
        }
		cout << out.str();
	}
	double getSeq( vector< string > c, int pos){
        //RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        int i;
        vector <double> owp;
        for(i=0;i<c.size();i++)
            OWP(c,i,owp);
        return 0.25 * winP(c, pos) + 0.5 * owp[pos] + 0.25 * OOWP(c, owp, pos);
    }
    double winP(vector<string> c, int pos){
        int i,tot=0, num=0;
        for(i=0;i<c.size();i++){
            if(i != pos && c[pos][i] != '.' ){
                num++;
                if(c[pos][i] == '1')    tot++ ;
            }
        }
        //cout << "winP: " << (double)tot / num << ", ";
        return (double)tot / num;
    }
    double winOP(vector< string >c, int pos,int without){
        int i,tot=0, num=0;
        if(cache[pos][without] != -10 ) return cache[pos][without];
        if(c[pos][without] == '.')  return -1;
        for(i=0;i<c.size();i++){
            if(i != pos && c[pos][i] != '.' && i != without){
                num++;
                if(c[pos][i] == '1')    tot++ ;
            }
        }
        //cout << "winOP of " << pos<< ":" <<  (double)tot / num<<endl;
        cache[pos][without] = (double)tot / num;
        return (double)tot / num;
    }
    double OOWP(vector< string >c, vector<double>owp, int pos){
        int i,num=0;
        double tot;
        for(i=0;i<owp.size();i++)
          if(i != pos && c[pos][i] != '.'){
            tot += owp[i];
            num++;
          }
       // cout << "OOWP: " << tot/num  << ", ";
        return tot/num;
    }
    double OWP(vector< string >c, int pos, vector<double> &owp){
        int i,num=0;
        double tot = 0,tmp;
        for(i=0;i<c.size();i++){
            if(i != pos){
                if( (tmp=winOP(c, i, pos)) >= 0){
                    num++;
                    tot += tmp;
                    //owp.push_back(tmp);
                }
                //else    owp.push_back(0);
            }
        }
        //cout << "OWP: " << tot/num << ", ";
        owp.push_back(tot/num);
        return tot/num;
    }
};


 void getContent(vector< vector<string> > &c){
    int i,j,k,cases, numC;
	scanf("%d\n", &cases);
	for(i=0;i<cases;i++){
        scanf("%d\n", &numC);
        vector<string> task;
        char tmp[101];
        memset(tmp, '\0', sizeof(tmp));
        for(j=0;j<numC;j++){
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

	getContent(c);
   //print(c);
	//print(c);
	RPI *cs = new RPI();
	cs->start(c);
	return 0;
	//string out = bt->getTime(v);
}
