#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;


 typedef vector<string> vs;
 typedef vector<int> vi; 
 typedef vector<vi> vvi; 
 typedef pair<int,int> ii; 
 #define sz(a) int((a).size()) 
 #define pb push_back 
 #define all(c) (c).begin(),(c).end()



class Train
{
private:
    int convert(string time)
    {
        string hh=time.substr(0,time.find(":"));
        string mm=time.substr(time.find(":")+1);
        int timeInMins=0;
        timeInMins= ( (hh[0]-'0')*10 + (hh[1]-'0') ) * 60 + ( mm[0]-'0' )*10 + ( mm[1]-'0' );
        
        return timeInMins;
    }
public:
    int depart;
    int arrival;
    int needsTrain;     // 1 or 0 or -1
    int turnAroundTime;
    Train(){}
    Train(string d,string arr,int turn,int train=1)
    {
        depart=convert(d);
        arrival=convert(arr)+turn;
        needsTrain=train;
    }

    bool operator > (const Train& T)
    {
        if( this->depart > T.depart )
            return true;
        return false;
    }

    bool operator < (const Train& T)
    {
        if(this->depart < T.depart)
            return true;
        return false;
    }
};

Train fromA[101];
Train fromB[101];
int compareAscending( const void* a, const void* b)
{
    return ( *(Train*)a > *(Train*)b );
}
int compareDescending(const void* a,const void* b)
{
    return ( (*(Train*)b).depart -  (*(Train*)a).depart);
}
int compareDescendingArrival(const void* a,const void*b)
{
    return ( (*(Train*)b).arrival - (*(Train*)a).arrival );
}


vector<int> process(int NA,int NB)
{
    vector<int> ret(2,0);
    qsort(fromA,NA,sizeof(Train),compareDescendingArrival);
    qsort(fromB,NB,sizeof(Train),compareDescending);

    for(int i=0;i<NA;i++)
    {
        for(int j=0;j<NB;j++)
        {
            if((fromA[i].arrival <= fromB[j].depart)&& (fromB[j].needsTrain>0) )
            {
                fromB[j].needsTrain--;
           //     fromA[i].needsTrain = (fromA[i].needsTrain<1)?fromA[i].needsTrain++:fromA[i].needsTrain;
                break;
            }
        }
    }
    qsort(fromB,NB,sizeof(Train),compareDescendingArrival);
    qsort(fromA,NA,sizeof(Train),compareDescending);
    for(int i=0;i<NB;i++)
    {
        for(int j=0;j<NA;j++)
        {
            if( (fromB[i].arrival<= fromA[j].depart) && (fromA[j].needsTrain>0) )
            {
                fromA[j].needsTrain--;
              //  fromB[i].needsTrain= (fromB[i].needsTrain<1)?++fromB[i].needsTrain:fromB[i].needsTrain;
                break;
            }
        }
    }

    for(int i=0;i<NA;i++)
        ret[0]+=fromA[i].needsTrain;
    for(int i=0;i<NB;i++)
        ret[1]+=fromB[i].needsTrain;
    return ret;
}

int main()
{
    ifstream inFile("B-large.in");
    ofstream outFile("B-Small.out");
    int N=0,T=0,NA=0,NB=0;
    string dep="",arr="";
    /*vector<Train> fromA;
    vector<Train> fromB;*/
    vector< vector<int> > op;
    
    inFile>>N;

    while (N>0)
    {
        inFile>>T>>NA>>NB;
        for(int i=0;i<NA;i++)
        {
            inFile>>dep>>arr;
            //fromA.push_back( Train(dep,arr) );
            fromA[i]=Train(dep,arr,T);
        }
        
        for(int i=0;i<NB;i++)
        {
            inFile>>dep>>arr;
            //fromB.push_back( Train(dep,arr) );
            fromB[i]=Train(dep,arr,T);
        }
        
        op.push_back( process(NA,NB) );
        /*fromA.clear();
        fromB.clear();*/
        N--;
    }

    for(int i=0;i<op.size();i++)
    {
        outFile<<"Case #"<<i+1<<":"<<" "<<op[i][0]<<" "<<op[i][1]<<endl;
    }
    
    return 0;
}