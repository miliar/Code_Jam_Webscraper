#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>

using namespace std;


class mytime
{
    public:
        int hour;
        int minute;
        mytime ()
        {
            hour=0;minute=0;
        }
        mytime(string s)
        {
            hour=atoi(s.substr(0,2).c_str());
            minute=atoi(s.substr(3).c_str());
        }
        mytime(int h,int m)
        {
            hour=h;
            minute=m;
        }
        mytime* settime (string s1)
        {
            hour=atoi(s1.substr(0,2).c_str());
            minute=atoi(s1.substr(3).c_str());
            //cout <<"s1="<<s1 <<" hour="<<hour<<" min="<<minute<<endl;
            return this;
        }
        void print()
        {
            cout<<hour<<":"<<minute;
        }
        std::string stringify()
        {
            std::ostringstream o;
            o << hour<<":"<<minute;
            return o.str();
        }

        mytime add(int t)
        {
            int mymin,myhour;
            myhour=hour;
            mymin=minute+t;
            if (mymin>=60){
                myhour=hour+(int)(mymin/60);
                mymin=mymin%60;
            }
            return mytime(myhour,mymin);
        }

        int subtract(mytime t1)
        {
            return ((t1.hour*60)+(t1.minute)) - ((hour*60)+(minute));
        }
};


class train
{
    public:
        mytime arrival,departure;
        bool used;
};

int main(int argc, char** argv)
{

    if (argc != 2 ) return 1;

    ifstream inFile;
    train trainAB[100],trainBA[100];
    string str,str1,str2;
    int casecount=0,count=0;

    inFile.open(argv[1],ios::in);

    inFile >> casecount;
    //cout <<"CASES="<<casecount<<endl;

    for(count=0;count<casecount;count++)
    {

        int T,NA,NB;
        inFile >> T;
        inFile >> NA>>NB;
        //cout <<"T="<<T<<" NA="<<NA<<" NB="<<NB;
        for (int i=0;i<NA;i++){
            inFile >> str1 >>str2;
            trainAB[i].departure.settime(str1);
            trainAB[i].arrival.settime(str2);
            trainAB[i].used=false;
        }
        for (int j=0;j<NB;j++){
            inFile >> str1 >> str2;
            trainBA[j].departure.settime(str1);
            trainBA[j].arrival.settime(str2);
            trainBA[j].used=false;
        }

        //calculation logic begins
        int TA=NA;
        int TB=NB;
        int matchindex,matchdiff;
        int diff=0;

        for (int i=0;i<NA;i++){
            matchindex = -1;
            matchdiff=1441;
            for (int j=0;j<NB;j++){
                if (trainBA[j].used == true)  continue;
                diff = trainAB[i].arrival.subtract(trainBA[j].departure);
                //cout << "BtoA:: i=" << i <<" j="<<j<<" diff="<<diff<<endl;

                if ( diff >= T && diff <= matchdiff){
                    matchindex = j;
                    matchdiff = diff;
                }
            }
            if (matchindex != -1){
                trainBA[matchindex].used = true;
                TB--;
                //cout << "found reusable train from B to A"<<trainBA[matchindex].departure.stringify()<<"  TB="<<TB<<endl;
            }
        }

        for (int i=0;i<NB;i++){
            matchindex = -1;
            matchdiff=1441;
            for (int j=0;j<NA;j++){
                if (trainAB[j].used == true)  continue;
                diff = trainBA[i].arrival.subtract(trainAB[j].departure);
                //cout << "AtoB:: i=" << i <<" j="<<j<<" diff="<<diff<<endl;
                if ( diff >= T && diff <= matchdiff){
                    matchindex = j;
                    matchdiff = diff;
                }
            }
            if (matchindex != -1){
                trainAB[matchindex].used = true;
                TA--;
                //cout << "found reusable train from A to B"<<trainAB[matchindex].departure.stringify()<<"  TA="<<TA<<endl;
            }
        }
        cout<<"Case #"<<count+1<<": "<<TA<<" "<<TB<<endl;

//        for (int i=0;i<NA;i++)  cout<<"Usage Train AB:"<<i<<"="<<trainAB[i].used<<endl;
//        for (int i=0;i<NB;i++)  cout<<"Usage Train BA:"<<i<<"="<<trainBA[i].used<<endl;
    }

    return 0;
}
