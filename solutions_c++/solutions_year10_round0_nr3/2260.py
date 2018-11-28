#include <iostream>
#include <list>
using namespace std;

int main(){
    unsigned cas; 
    cin>>cas;
    unsigned long long result[cas];
    for(int cc=0; cc<cas; cc++){
        unsigned long long R,k,Cost,kfill;
        unsigned  N;
        cin >>R>>k>>N; 
        unsigned nind,pind; // pind denotes the start of grps already in swing
        nind=0;pind=0;        //nind denotes where to pick up next 
        unsigned long long *gi= new unsigned long long[N];
        unsigned long long *costpre = new unsigned long long[N]; // cost bypass thru cache
        unsigned *nind_pre = new unsigned [N]; //next index bypass thru cache
        bool *index_seen = new bool [N];// index already seen ,, no need to calculate
        for(unsigned g=0;g<N;g++){
           unsigned long long tmp;  
           cin  >> tmp; 
           gi[g]=tmp;
           index_seen[g] =false;
        }
        Cost=0; 
        for(unsigned long long r=0;r<R;r++){
            kfill =0;         
            if(index_seen[nind]){ // index is observed.. no need to calculate
              //Hit will occur here... load the kfill <=> cost of one ride and the next index
                kfill = costpre[nind];
                nind = nind_pre[nind];
                }
            else{    
              //Miss will occur here
             while(kfill+gi[nind]<=k){ //if the next group can be accomodated;
               kfill += gi[nind]; //kfill < fill the ride
               nind = (nind+1)%N;   //index rolls arund no need for data shifting
               if(nind==pind) break;                        
             }
            }
            //load the cache and cost
            costpre[pind]=kfill;
            nind_pre[pind]=nind; 
            index_seen[pind]=true;
            pind = nind; //pind is the index before which evyone gone to ride last time
            Cost+= kfill;   //increment cost
        }
        delete gi;
        delete costpre;
        delete nind_pre;
        delete index_seen;
        
        cout <<"Case #"<<cc+1<<": "<< Cost<<endl;
           
    }
   
}
