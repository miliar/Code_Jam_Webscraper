#include <iostream>
#include <fstream>
#include <list>

using namespace std;

int main(int argc, char *argv[0])
{
 unsigned int R, K, T, N;
 unsigned int i, tmp, tmpN, curPeople, curMoney = 0;
 ofstream out;
 ifstream in;
 list<unsigned int> Q;

        if(argc != 3)
        { cerr << "Use : " << argv[0] << " input output" <<endl; return -1; }

        in.open(argv[1]);
        if(!in.is_open())
        { cerr << "File IO error." << endl; return -1; }

        out.open(argv[2]);
        if(!out.is_open())
        { cerr << "File IO error." << endl; return -1; }

        //Get to the point
        in >> T;

        for(unsigned int casesNum=0; casesNum < T; casesNum++)
        {
            in >> R >> K >> N;
            out << "Case #" << casesNum+1 << ": ";

            //Read Queque
            for(i=0; i<N; i++)
            { in >> tmp;  Q.push_back(tmp); }

            //Each round
            for(i=curPeople=curMoney=0; i<R; i++,curPeople=0)
            {
                tmp = *(Q.begin());
                tmpN = N;

                while(tmpN--)
                {
                    if((tmp+curPeople) > K)
                        break;

                    curPeople += tmp;
                    curMoney  += tmp;

                    Q.pop_front();
                    Q.push_back(tmp);

                    tmp = *(Q.begin());
                }
            }

            //Empty list
            Q.clear();
            out << curMoney << endl;
        }

        in.close();
        out.close();

 return 0;
}
