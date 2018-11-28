#include <myincludes.h>

#define FILE_IN "C-small-attempt1.in"
#define FILE_OUT "C-small-attempt1.out"

using namespace std;

void Solve(ifstream &iFile, ofstream &oFile)
{
    BigUnsigned i;
    int j;
    int n;
    BigUnsigned l,h;

    iFile >>n;
    l = GetUnsinged(iFile);
    h = GetUnsinged(iFile);

    vector<BigUnsigned> play;

    for(j=0;j<n;j++)
    {
        BigUnsigned tmp;
        tmp = GetUnsinged(iFile);
        play.push_back(tmp);
    }

    for(i=l;i<=h;i++)
    {
        bool check = true;
        for(j=0;j<n;j++)
        {
            BigUnsigned rem;
            BigUnsigned other;
            BigUnsigned tmp2;
            if(play[j]>i)
            {
                rem = play[j];
                other = i;
            }
            else
            {
                rem = i;
                other = play[j];
            }

            rem.divideWithRemainder(other,tmp2);

            if(rem != 0)
            {
                check = false;
                break;
            }
        }
        if(check)
        {
            oFile <<i <<endl;
            return;
        }
    }
    oFile<< "NO" <<endl;
    return;
}

//void Solve(ifstream &iFile, ofstream &oFile)
//{
//    int i;
//    int n;
//    BigUnsigned l,h;
//
//    iFile >> n;
//
//    l = GetUnsinged(iFile);
//    h = GetUnsinged(iFile);
//
//    vector<BigUnsigned> play;
//
//    for(i=0;i<n;i++)
//    {
//        BigUnsigned tmp;
//        tmp = GetUnsinged(iFile);
//        play.push_back(tmp);
//    }
//
//    BigUnsigned divisor = play[0];
//    for(i=1;i<n;i++)
//    {
//        divisor = gcd(divisor,play[i]);
//        if(divisor < l)
//        {
//            oFile << "NO" <<endl;
//            return;
//        }
//    }
//
//    BigUnsigned newD = divisor;
//
//
//    BigUnsigned rem1 = newD;
//    BigUnsigned num1;
//    rem1.divideWithRemainder(l,num1);
//
//    BigUnsigned rem2 = newD;
//    BigUnsigned num2;
//    rem2.divideWithRemainder(h,num2);
//
//    if(rem1 == 0)
//    {
//        oFile << l <<endl;
//        return;
//    }
//    else
//    {
//        num1--;
//        if(rem2!=0)
//        {
//            num2++;
//        }
//
//        if(num2!=num1)
//        {
//            BigUnsigned find;
//            for(find = num1;find>=num2;find--)
//            {
//                BigUnsigned x;
//                BigUnsigned rem3 = newD;
//                rem3.divideWithRemainder(find,x);
//                if(rem3 == 0)
//                {
//                    oFile << x <<endl;
//                    return;
//                }
//            }
//        }
//        oFile << "NO" <<endl;
//        return;
//    }
//
//}

int main()
{
    ifstream iFile(FILE_IN);
    ofstream oFile(FILE_OUT);;

    int caseNum;
    if(!iFile.is_open())
    {
        cout << "iFile not open!" <<endl;
    }
    iFile >> caseNum;

    int i;

    for(i=0;i<caseNum;i++)
    {
        oFile <<"Case #" <<i+1 <<": ";

        Solve(iFile,oFile);
    }

    iFile.close();
    oFile.close();

    return 0;
}
