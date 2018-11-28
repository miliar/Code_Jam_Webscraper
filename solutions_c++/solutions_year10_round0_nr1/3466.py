#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

struct snp{
    bool pwr;
    bool on;
    unsigned short n;
};
int main(){
ifstream fin("A-large.in");
ofstream fout("A-large.out");
unsigned short cases=0;

fin>>cases;
snp nums[cases];
unsigned int claps[cases];
memset(&nums,0,sizeof(nums));
memset(&claps,0,sizeof(claps));

for(unsigned short i=0;i<cases;i++){
    fin>>nums[i].n >>claps[i];
}
for(unsigned short i=0;i<cases;i++){
    if(claps[i]>=nums[i].n){
        if(nums[i].n==1){
                nums[i].pwr=true;
                if(((claps[i]+1)/1)%2==0){
                    nums[i].on=true;
                }
                else{
                    nums[i].on=false;
                }
        }
        else{
            if (((claps[i]+1)% (unsigned int)(pow(2,(nums[i].n-1))))==0){
                nums[i].pwr=true;
                if(((claps[i]+1)/(unsigned int)(pow(2,(nums[i].n-1))))%2==0){
                    nums[i].on=true;
                }
            }
            else{
                nums[i].pwr=false;
                nums[i].on=false;
            }
        }
    }
    else{
        nums[i].pwr=false;
        nums[i].on=false;
    }
    if(nums[i].on==true){
        fout<<"Case #"<<i+1<<": ON"<<endl;
    }
    else{
        fout<<"Case #"<<i+1<<": OFF"<<endl;
    }
}
}
