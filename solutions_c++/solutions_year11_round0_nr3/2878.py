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

class CandySplit{
public:
    int va,vb;
	void start(vector< vector<int> >c ){
		int i,num;
		stringstream out(stringstream::in | stringstream::out);
		
		for(i=0;i<c.size();i++){
            sort(c[i].begin(),c[i].end());
            num = getSeq(c[i]);
            if(num < 0)
    			out << "Case #" << (i+1) << ": NO" << endl;
    		else
    		   out << "Case #" << (i+1) << ": "<< num << endl;
        }
		cout << out.str();
	}
	int getSeq( vector<int> c){
        int i;
        vector<bool> status;
        
        for(i=0;i<c.size();i++)
            status.push_back(false);
            
        for(i=1;i<c.size();i++){  
            refresh(status);
            if(calNum(c, i, status,true)) 
                return max(va, vb);
        }
		return -1 ;
	}
	bool calNum(vector<int> c, int num, vector<bool> status,bool init){
        int i;
        if(num == 0)    return getVal(c, status, 0) == getVal(c, status,1);
        for(i=0;i<c.size();i++){
            //if(check(status))   cout << "calNum: status is fresh, num = " << num <<endl;
            if(!status[i]){
                status[i] = true;
                if(calNum(c, num-1, status, false)){
                    if(init){    
                        va = getTrueVal(c, status,0);
                        vb = getTrueVal(c, status,1);
                    }
                    return true;
                }
            }
        } 
        return false;
    }
	void refresh(vector<bool> &status){
        int i;
        for(i=0;i<status.size();i++)
            status[i] = false;
    }
    bool check(vector<bool>status){
        int i;
        for(i=0;i<status.size();i++)
            if(status[i])   return false;
        return true;
    }
    void printStatus(vector<bool>status){
        int i;
        for(i=0;i<status.size();i++)
            cout << status[i] << " ";
        cout << endl;
    }
	int max(int a,int b){return a>b?a:b;}

	int getVal(vector<int> c, vector<bool>  status, int flag){
        int i,tot=0;
        if(flag==0){
            for(i=0;i<c.size();i++)
                if(status[i])   tot ^=c[i];
        }
        if(flag==1){
            for(i=0;i<c.size();i++)
                if(!status[i])   tot^=c[i];
        }
        return tot;
    }
    int getTrueVal(vector<int> c, vector<bool>  status, int flag){
        //cout << "getTrueVal: " ;
        //printStatus(status);
        int i,tot=0;
        if(flag==0){
            for(i=0;i<c.size();i++)
                if(status[i])   tot +=c[i];
        }
        if(flag==1){
            for(i=0;i<c.size();i++)
                if(!status[i])   tot+=c[i];
        }
        return tot;
    }
	
};


 void getContent(vector< vector< int > > &c){
    int i,j,cases, numC;
	scanf("%d\n", &cases);
	for(i=0;i<cases;i++){
        scanf("%d\n", &numC);
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
	CandySplit *cs = new CandySplit();
	cs->start(c);
	return 0;
	//string out = bt->getTime(v);
}
