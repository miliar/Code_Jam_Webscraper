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

class Booster{
public:
	void start(vector< vector< int > > &c, vector< vector< int > > &unit , vector< vector< int > > &dis ){
		int i,j;
		stringstream out(stringstream::in | stringstream::out);
		for(i=0;i<c.size();i++){
    		out << "Case #" << (i+1) << ": " ;
    		//cout << "case " << i<< "..." <<endl;
                out << getSeq(c[i], unit[i], dis[i]) << endl;
        }
		cout << out.str();
	}
	int getSeq( vector< int > c, vector<int> unit, vector< int > dis ){
        int i,tot = 0, num = c[0],cur,cut,time=0, dis2;
        vector<int>over;
        int total = getTotal(dis);
        //sort(unit.begin(),unit.end());
        cut = getCutPoint(c, dis, dis2);
        //cout << "getSeq: cut = " <<cut << ", dis.size() = " << dis.size() <<endl;
        int size = dis.size();
        for(i=cut+1;i<size;i++)
            over.push_back(dis[i]);
            
        int cuttime = (c[1] - dis2 * 2) + dis[cut] - (c[1] - dis2 * 2)/2;
        int saving = dis[cut]*2 - cuttime;
            
        int osize = over.size();
        bool addCut = false;
        int tdis = 0;
        if(osize > 0){
            //cout <<"in over" <<endl;
            sort(over.begin(),over.end());
            for(i=num;i>0;i--){
                if(over.size() == 0){
                    time += cuttime;
                    tdis += dis[cut];
                    break;
                }
                if(over.back() > saving){
                    time += over.back();
                    tdis += over.back();
                    over.pop_back();
                }
                else if(addCut){    //already added
                    time += over.back();
                    tdis += over.back();
                    over.pop_back();
                }
                else{    //< cuttime and not added
                     time += cuttime;
                     tdis += dis[cut];
                     addCut = true;
                }
            }
            //cout << "after over: time = " <<time <<endl;
            time += (total - tdis) * 2;
                //time += dis2 * 2;
            //cout << "i = 0, time = " <<time <<endl;
            /*if(i > 0){      //limited over 
                time += (c[0] - dis2 * 2) + (dis[i] - (c[0] - dis2 * 2)/2);
                time += dis2 * 2;
                cout << "i>0, time = " <<time <<endl;
            }
            else{
                //for(i=0;i<over.size();i++)
                //    time += over[i] * 2;
                
            }   */
        }
        else{
            //cout << "over size = 0 "<<endl;
            // for(i=0;i<size;i++)
            time = total*2;
        }
        
        return time;
        //if(over.size() > 0) over.
    }
    int getTotal( vector< int > dis){
        int i,tot;
        for(i=0;i<dis.size();i++){
            tot+=dis[i];
        }
        return tot;
    }
    int getCutPoint(vector< int > c, vector< int > dis ,int &dis2){
        int i,tot=0;
        for(i=0;i<dis.size();i++){
            if( (tot + dis[i]) * 2 > c[1]){   
                //cout << "curpoint = " <<i<<endl;
                dis2 = tot ;
                return i;
            }
            else tot += dis[i];
        }
        return -1;
    }
};


 void getContent(vector< vector<int> > &c, vector< vector<int> > &dis, vector< vector<int> > &unit){
    int i,j,k,cases, L, t, N, C,tmp,cur;
	scanf("%d\n", &cases);
	//cout << "getContent: case = " << cases<<endl;
	for(i=0;i<cases;i++){
        scanf("%d %d %d %d", &L, &t, &N, &C);
        vector<int> task;
        vector<int>list;
        vector<int>_dis;
        vector<int>_unit;
        task.push_back( L );
        task.push_back( t );
        task.push_back( N );
        task.push_back( C );
        for(j=0;j<C;j++){
            scanf("%d", &tmp);
            list.push_back(tmp);
        }
        //scanf("\n");
        cur = 0;
        int last = 0;
        for(j=0;j<N;j++){
            _dis.push_back(list[cur] );
            _unit.push_back(list[cur] );
            //last = list[cur] + last;
            cur = (cur+1)%C;
        }
        dis.push_back(_dis);
        unit.push_back(_unit);
        c.push_back(task);    
    }
}
    
void print(vector< vector<int> >c){
     int i,j;   
     //cout <<"print: size = " <<c.size() <<endl;
     for(i=0;i<c.size();i++){
        for(j=0;j<c[i].size();j++)
            cout << c[i][j] << " ";
        cout << endl;
    }
}
  
int main(int argc, char *argv[]){
	vector< vector< int > > c;
	vector< vector< int > > dis;
	vector< vector< int > > unit;
    //cout <<"in main"<<endl;
	getContent(c,dis,unit);
    //print(c);
    //print(dis);
	//print(c);
	Booster *cs = new Booster();
	cs->start(c,unit,dis);
	return 0;
	//string out = bt->getTime(v);
}
