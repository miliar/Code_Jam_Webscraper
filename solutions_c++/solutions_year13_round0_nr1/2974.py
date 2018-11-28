#include "iostream"
#include "iomanip"
#include "vector"
#include "numeric"
#include <string>
#include "fstream"
using namespace std;

const int ROW = 4;
const int LINE = 4;
const string A="X won";
const string B="O won";
const string C="Draw";
const string D="Game has not completed";



string test(string str){
     const int MAX = 1000;
    vector< int > inputs(ROW*LINE);
    typedef vector<int> ivec;

    for(int i=0;i<inputs.size();++i){

        switch(str.at(i)){
            case 'X':inputs[i]=1;break;
            case 'O':inputs[i]=-1;break;
            case 'T':inputs[i]=0;break;
            case '.':inputs[i]=MAX;break;
        }
    }
    int sum;
    bool isOver;


    string outs;
    for(ivec::size_type i=0;i<ROW;++i){
        //ÐÐ
        sum = 0;
        for(ivec::size_type j=0;j<LINE;++j){
            sum += inputs[i*LINE+j];
        }
        if(sum>=3&&sum<5){
            outs = A;
            isOver= true;
            break;
        }else if(sum<=-3){
            outs=B;
            isOver= true;
            break;
        }
    }
    if(!isOver){
        for(ivec::size_type i=0;i<LINE;++i){
            //ÁÐ
             sum = 0;
            for(ivec::size_type j=0;j<ROW;++j){
                sum += inputs[i+j*ROW];
            }
            if(sum>=3&&sum<5){
                outs = A;
                isOver = true;
                break;
            }else if(sum<=-3){
                outs=B;
                isOver = true;
                break;
            }
        }
    }
    if(!isOver){
        //diag
        sum = 0;
        for(ivec::size_type i=0;i<ROW;++i){
            sum += inputs[i*ROW+i];
        }
        if(sum>=3&&sum<5){
            outs = A;
            isOver = true;
        }else if(sum<=-3){
            outs=B;
            isOver = true;
        }
    }
    if(!isOver){
        //diag2
        sum = 0;
        for(ivec::size_type i=0;i<ROW;++i){
            sum += inputs[i*ROW+(ROW-i-1)];
        }
        if(sum>=3&&sum<5){
            outs = A;
            isOver = true;
        }else if(sum<=-3){
            outs=B;
            isOver = true;
        }
    }
    if(!isOver){
       sum=accumulate(inputs.begin(),inputs.end(),0);
       if(sum>5){
        outs = D;
       }else{
        outs=C;
       }
    }
    return outs;
}

int main(void)
{

    fstream ifs("A-large.in",ios_base::in);
    fstream ofs("A_large.ou",ios_base::out);

    int times;
    ifs>>times;
   for(int i=0;i<times;++i){
        string strIn="",str;
        for(int j=0;j<ROW;++j){
            ifs>>str;
            strIn+=str;
        }
        ofs<<"Case #"<<i+1<<": "<<test(strIn)<<endl;
    }
    ifs.close() ;
    ofs.close();
    return 0;
}

