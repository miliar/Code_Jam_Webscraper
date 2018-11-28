
#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<climits>
#include<iomanip>
#include<iterator>

#define F0M(I,MAX) for(int I=0;I!=MAX;++I)
#define FPM(I,P,MAX) for(int I=P;I!=MAX;++I)
#define MAX(x,y,z)(((MAX(x,y))>(z))?(((MAX(x,y)):(z)))
#define MIN(x,y,z)(((MIN(x,y))<(z))?(((MIN(x,y)):(z)))
#define MAX(x,y)(((x)>(y))?(x):(y))
#define MIN(x,y)(((x)<(y))?(x):(y))
//copy(v.begin(), v.end(), ostream_iterator<string>(cout, "\n"));

using namespace std;
//
//void magicKa()
//{
////    ifstream fin("C:\\Users\\jrying\\Downloads\\A-lagre.in");
////    ofstream fout("C:\\Users\\jrying\\Downloads\\A-large.out");
//
////    ifstream fin("C:\\Users\\jrying\\Downloads\\B-small-attempt1.in");
////    ofstream fout("C:\\Users\\jrying\\Downloads\\B-small.out");
//
//    ifstream fin("C:\\Users\\jrying\\Downloads\\B-test.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\B-test.out");
//
//    int N;fin>>N;
//    F0M(i,N)
//    {
//        int C, D, M;
//        vector<string> ci;
//        vector<char> co;
//        vector<string> cd;
//        string input;
//
//        fin>>C;
//        F0M(j,C)
//        {
//            string t; fin>>t;
//            string t2(t, 0, 2);
//            ci.push_back(t2);
//            swap(t2[0], t2[1]);
//            ci.push_back(t2);
//            co.push_back(t[2]);
//            co.push_back(t[2]);
//        }
//        fin>>D;
//        F0M(j,D)
//        {
//            string t; fin>>t;
//            cd.push_back(t);
//            swap(t[0], t[1]);
//            cd.push_back(t);
//        }
//        fin>>M;
//        fin>>input;
//        reverse(input.begin(), input.end());
//        int pos = 0;
//        while(1)
//        {
//            int minpos = INT_MAX;
//            int minw = 0;
//            bool com;
//            F0M(j,2*C)
//            {
//                int open = input.find(ci[j], pos);
//                if(minpos > open && open != string::npos)
//                {
//                    minpos = open+1;
//                    minw = j;
//                    com = 1;
//                }
//                cout<<"cc "<<input<<" "<<minpos<<endl;
//            }
//            F0M(j,2*D)
//            {
//                int open = input.find(cd[j][0]);
//                int close = input.find(cd[j][1], pos);
//                if(close != string::npos && open != string::npos &&open < minpos)
//                {
//                    minpos = open;
//                    minw = j;
//                    com = 0;
//                }
//                cout<<"dd "<<input<<open<<" "<<close<<" "<<minpos<<endl;
//            }
//            if(minpos == INT_MAX) //find next open
//            {
//                F0M(j,2*D)
//                {
//                    minpos = MIN(input.find(cd[j][0], pos+1), minpos);
//                }
//                if(minpos == INT_MAX)break;
//                else {pos = minpos; continue;}
//            }
//            if(com)
//            {
//                string t(1, co[minw]);
//                input.replace(minpos-1, 2, t);
//                pos = MAX(minpos-1, 0);
//            }
//            else
//            {
//                int end = input.find(cd[minw][1]);
//                input.erase(minpos, end-minpos+1);
//                pos = MAX(minpos-1, 0);
//            }
//        }
//        reverse(input.begin(), input.end());
//        if(input.length() != 0)
//        {
//            fout<<"Case #"<<i+1<<": [";
//            copy(input.begin(), input.end()-1, ostream_iterator<char>(fout, ", "));
//            fout<<input[input.length()-1]<<"]"<<endl;
//        }
//        else fout<<"Case #"<<i+1<<": []"<<endl;
//
//    }
//}



void magicKa()
{
//    ifstream fin("C:\\Users\\jrying\\Downloads\\A-lagre.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\A-large.out");

    ifstream fin("C:\\Users\\jrying\\Downloads\\B-large.in");
    ofstream fout("C:\\Users\\jrying\\Downloads\\B-large.out");

//    ifstream fin("C:\\Users\\jrying\\Downloads\\B-test.in");
//    ofstream fout("C:\\Users\\jrying\\Downloads\\B-test.out");

    int N;fin>>N;
    F0M(i,N)
    {
        int C, D, M;
        vector<string> ci;
        vector<char> co;
        vector<string> cd;
        string input;

        fin>>C;
        F0M(j,C)
        {
            string t; fin>>t;
            string t2(t, 0, 2);
            ci.push_back(t2);
            swap(t2[0], t2[1]);
            ci.push_back(t2);
            co.push_back(t[2]);
            co.push_back(t[2]);
        }
        fin>>D;
        F0M(j,D)
        {
            string t; fin>>t;
            cd.push_back(t);
            swap(t[0], t[1]);
            cd.push_back(t);
        }
        fin>>M;
        fin>>input;

        int pos = 0;
        while(1)
        {
            int minpos = INT_MAX;
            int minw = 0;
            bool com;

            F0M(j,2*D)
            {
                int close = input.find(cd[j][1], pos);
                if(close == string::npos)continue;
                int open = input.rfind(cd[j][0], close);
                if(open != string::npos && close < minpos)
                {
                    minpos = close;
                    minw = j;
                    com = 0;
                }
//                cout<<"dd "<<input<<" "<<open<<" "<<close<<" "<<minpos<<endl;
            }
            F0M(j,2*C)
            {
                int open = input.find(ci[j], pos);
                if(open != string::npos && open < minpos)
                {
                    minpos = open;
                    minw = j;
                    com = 1;
                }
//                cout<<"cc "<<input<<" "<<open<<" "<<minpos<<endl;
            }
            if(minpos == INT_MAX) //find next open
            {
                F0M(j,2*D)
                {
                    minpos = MIN(input.find(cd[j][0], pos+1), minpos);
                }
                if(minpos == INT_MAX)break;
                else {pos = minpos; continue;}
            }
            if(com)
            {
                string t(1, co[minw]);
                input.replace(minpos, 2, t);
                pos = MAX(minpos, 0);
            }
            else
            {
                input.erase(0, minpos+1);
                pos = 0;
//                int open = input.rfind(cd[minw][0], minpos);
//                input.erase(open, minpos-open+1);
//                pos = MAX(open, 0);
            }
        }

        if(input.length() != 0)
        {
            fout<<"Case #"<<i+1<<": [";
            copy(input.begin(), input.end()-1, ostream_iterator<char>(fout, ", "));
            fout<<input[input.length()-1]<<"]"<<endl;
        }
        else fout<<"Case #"<<i+1<<": []"<<endl;

    }
}




int main()
{
    magicKa();
}
//
//C D N
//5
//0 0 2 EA
//1 QRI 0 4 RRQR
//1 QFT 1 QF 7 FAQFDFQ
//1 EEZ 1 QE 7 QEEEERA
//0 1 QW 2 QW
//	Case #1: [E, A]
//Case #2: [R, I, R]
//Case #3: [F, D, T]
//Case #4: [Z, E, R, A]
//Case #5: []
