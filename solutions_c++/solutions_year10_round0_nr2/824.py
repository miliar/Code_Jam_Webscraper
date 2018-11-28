#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include "biginteger/BigIntegerLibrary.hh"

using namespace std;
#define INFILENAME "bs.in"
#define OUTFILENAME "bs.out"

class Data{
public:
    int num;
    BigUnsigned *time;
};

class Env{
public:
    int testcase;
    Data *data;
    char *inname, *outname;

    int init(char *, char *);
    int factorize(BigUnsigned, vector<int> *);
    int exec();
};

int Env::init(char *in, char *out){
    FILE *fin;
    char buf[128];

    inname = in;
    outname = out;

    fin = fopen(inname,"r");
    if(fin == NULL){
        printf("cant open\n");
        return 0;
    }

    fscanf(fin, "%d\n", &testcase);
    data = new Data[testcase];
    for(int i=0;i<testcase;i++){
        fscanf(fin, "%d ", &data[i].num);
        data[i].time = new BigUnsigned[data[i].num];
        for(int k=0;k<data[i].num;k++){
            fscanf(fin, "%s ", buf);
            data[i].time[k] = stringToBigUnsigned(buf);
            //printf("|%s,%s| ", buf,bigUnsignedToString(data[i].time[k]).c_str());
        }
        //printf("\n");
    }
    
    fclose(fin);
}

int Env::exec(){
    FILE *fout;
    int n, k;
    BigUnsigned tmp, a, b, ans;
    vector<BigUnsigned> v;
    fout = fopen(outname, "w");
    if(fout == NULL){
        printf("cant open\n");
        return 0;
    }

    for(int i=0;i<testcase;i++){
        for(int j=0;j<data[i].num;j++){
            for(int k=j+1; k<data[i].num;k++){
                a = data[i].time[j];
                b = data[i].time[k];
                
                
                if(a > b)
                    tmp = a - b;
                else
                    tmp = b - a;

                if(tmp != 0)
                    v.push_back(tmp);
            }
        }

        if(v.size() > 0){
            vector<BigUnsigned>::iterator it=v.begin();
            tmp = *it++;
            while(it != v.end()){
                a = *it++;
                //printf(">tmp:%s a:%s\n", bigUnsignedToString( tmp ).c_str(), bigUnsignedToString( a ).c_str());
                tmp = gcd(tmp, a);
                //printf(">>tmp:%s\n", bigUnsignedToString( tmp ).c_str());
            }
            //printf(">>gcd:%s\n", bigUnsignedToString( tmp ).c_str());

            a = data[i].time[0];
            ans = ((((a-1) / tmp) + 1) * tmp) - a;
            //printf(">>Answer:%s\n", bigUnsignedToString( ans ).c_str());
        }else{
            ans = 0;
        }
        // for(vector<BigUnsigned>::iterator it=v.begin(); it != v.end(); it++){
        //     printf(">%s\n", bigUnsignedToString(*it).c_str() );
        // }
        // printf(">%s %s\n", bigUnsignedToString(data[i].time[0]).c_str(), bigUnsignedToString(data[i].time[1]).c_str());
        // printf(" %s\n", bigUnsignedToString(gcd(data[i].time[0], data[i].time[1])).c_str());
        // printf("ON  %d %d %d\n",n,k,tmp);
        fprintf(stdout, "Case #%d: %s\n", i+1, bigUnsignedToString( ans ).c_str());
        fprintf(fout, "Case #%d: %s\n", i+1, bigUnsignedToString( ans ).c_str());
        
        //printf("\n");
        v.clear();
    }
    
}

int main(void){
    
    Env *env;
    env = new Env;
    env->init((char *)INFILENAME, (char *)OUTFILENAME);
    env->exec();

    // BigInteger hoge;
    // hoge = stringToBigInteger("1000000000000000000000000");
    // printf("%s\n", bigIntegerToString(hoge).c_str());
    return 0;
}
