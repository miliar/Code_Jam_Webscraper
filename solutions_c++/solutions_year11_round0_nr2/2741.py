#include<stdio.h>
#include<iostream>
#include<sstream>
#include<vector>
#include<math.h>
#include<set>
#include<map>
//#include<pair>

using namespace std;

class Magicka{
public:
	void start(vector< set<string> >ma, vector< set<string> >mb, vector<  string > c, 
             vector< map<string, string> >amap ){
		int i;
		stringstream out(stringstream::in | stringstream::out);
		for(i=0;i<c.size();i++)
			out << "Case #" << (i+1) << ": [" << getSeq(ma[i],mb[i],c[i], amap[i]) << "]" << endl;
		cout << out.str();
	}
	string getSeq( set< string > a,  set< string > b, string c, map<string, string>amap){
        int i;
        string output= "";
        bool flag ;
        //cout << "getseq: " << c<<endl;
        for(i=1;i<c.size();i++){
            string _str = c.substr(0,i+1);
            int ori_size = _str.size();
            flag = true;
            while(flag && _str.size()>1)
                flag = checkComposite(_str, a, amap);
            checkOpposite(_str, b);
            c = _str + c.substr(i+1);
            if(_str != "")
                i -= ori_size - _str.size();
            else
                i = 0;
        }
        for(i=0;i<c.size();i++)
            output += c.substr(i,1) + ", " ;
        
		return output.substr(0, output.size()-2) ;

	}
	bool checkComposite(string &cur, set< string > ma, map<string, string> amap ){
        //cout << "checkComposite: target = " << cur.substr(cur.size()-2,2)<<endl;
        if( ma.count(cur.substr(cur.size()-2,2)) > 0) {
            cur = cur.substr(0,cur.size()-2) + amap[cur.substr(cur.size()-2,2)];
            //cout << "checkComposite: cur = " <<cur<<endl;
            return true;
        }
        return false;
	}	
	void checkOpposite(string &cur, set< string > mb){
        int i;
        for(i=0;i<cur.size()-1;i++){
    		if( mb.count(cur.substr(i,1) + cur.substr(cur.size()-1,1)) > 0)   {
                //cout  << "checkOpposite: cur = ''"<<endl;
                cur = "";
                return;
            } 
        }
	}


};


 void getContent(vector< vector< string > > &a, vector< vector< string > > &b, vector<  string > &c){
	int cases,i,j, num;
	char robot;

	scanf("%d\n", &cases);
	for(i=0;i<cases;i++){

		scanf("%d ", &num);	
		vector< string >tmp;
		for(j=0;j<num;j++){
			char combine[4];
			memset(combine, '\0', sizeof(combine));
			scanf("%3s", combine);
			tmp.push_back(combine);
		}
		a.push_back(tmp);
		scanf("%d ", &num);	
		vector< string >tmp2;
		for(j=0;j<num;j++){
			char combine[4];
			memset(combine, '\0', sizeof(combine));
			scanf("%2s", combine);
			tmp2.push_back(combine);
		}
		b.push_back(tmp2);
		scanf("%d ", &num);
		string tmp3;
		char combine[101];
		memset(combine, '\0', sizeof(combine));
		scanf("%s\n", combine);
		tmp3 = string(combine);
		c.push_back(tmp3);
		scanf("\n");          
	}
}
                        
 void getMap(vector< vector< string > > &a, vector< set<string> > &ma, vector< vector< string > > &b, vector< set<string> > &mb, vector< map<string, string> > &amap){
	int i,j;
	     
    //cout << "a.size = " << a.size()<< ", b.size() = " << b.size() <<endl;
	for(i=0;i<a.size();i++){
		set<string>m;
		map<string, string>am;
		for(j=0;j<a[i].size();j++){
			m.insert(a[i][j].substr(0,2));
			m.insert(a[i][j].substr(1,1)+a[i][j].substr(0,1));
			am[a[i][j].substr(0,2)] = a[i][j].substr(a[i][j].size()-1,1);
			am[a[i][j].substr(1,1)+a[i][j].substr(0,1)] = a[i][j].substr(a[i][j].size()-1,1);
		}
		ma.push_back(m);
		amap.push_back(am);
	}

  
	for(i=0;i<b.size();i++){
      	set<string>m;    
		for(j=0;j<b[i].size();j++){
			m.insert(b[i][j].substr(0,2));
			m.insert(b[i][j].substr(1,1)+b[i][j].substr(0,1));
		}
		mb.push_back(m);
	}                           
 }
 void print(vector< vector< string > > a, vector< vector< string > > b, vector<  string  > c, vector< map<string,string> >amap ){
	int i,j;
	for(i=0;i<a.size();i++){
		cout << i<<endl;
		cout <<" a: " ;
		for(j=0;j<a[i].size();j++){
			cout << a[i][j] <<" " ;
		}
		cout <<" b: " ;
		for(j=0;j<b[i].size();j++){
			
			cout << b[i][j] <<" ";
		}
		cout <<" c: " ;
		cout << c[i];

		map<string, string>::iterator it;
		if(amap[i].size() > 0){
            cout <<" map: " ;
    		for(it=amap[i].begin();it!=amap[i].end();it++){
               //cout <<"test"<<endl;
    			cout << (*it).first <<":" << (*it).second << " ," ;
    		}
        }
		cout << endl;
	}
 }
int main(int argc, char *argv[]){
	vector< vector< string > > a;
	vector< vector< string > > b;
	vector< string > c;
	vector< set<string> >ma;
	vector< set<string> >mb;
	vector< map<string, string> >amap;

	getContent(a,b,c);
	getMap(a,ma, b, mb, amap);
	//print(a,b,c,amap);
	Magicka *mg = new Magicka();
	mg->start(ma,mb,c,amap);
	return 0;
	//string out = bt->getTime(v);
}
