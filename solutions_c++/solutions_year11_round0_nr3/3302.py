#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>

int MAX_COOKIE_STRING_LENGTH = 20;

using namespace std;

string* cookieValues;
int* cookieValuesNo;
long long bestSum;


string addCookieValuesBinary(string cookie1, string cookie2)
{
    string result = "00000000000000000000";
    for (int i=0; i<MAX_COOKIE_STRING_LENGTH; i++)
    {
        if ((cookie1[i] == '1') && (cookie2[i]=='1'))
        {
            result[i] = '0';
        } else if ((cookie1[i] == '1') || (cookie2[i]=='1'))
        {
            result[i] = '1';
        } else {
            result[i] = '0';
        }
    }

    return result;
}

void g(int s[],int p,int k,int t[],int q=0,int r=0)
{
    if(q==k)
    {
        bool* cookiesCollected;
        cookiesCollected = new bool[p];

        for (int i=0;i<p;i++)
        {
            cookiesCollected[i]=false;
        }

        string tempSumSean = "00000000000000000000";
        string tempSumPatrick = "00000000000000000000";

        // compute Seans sum
        for(int i=0;i<k;i++)
        {
//            cout<<t[i];
            int test = t[i];
            cookiesCollected[t[i]] = true;
            tempSumSean = addCookieValuesBinary(tempSumSean,cookieValues[t[i]]);
        }


        for(int i=0;i<p;i++)
        {
            if (!cookiesCollected[i])
            {
                tempSumPatrick = addCookieValuesBinary(tempSumPatrick,cookieValues[i]);
            }
        }

        if (tempSumSean == tempSumPatrick)
        {
            long long currentSplitSum = 0;
            for (int i=0; i<k;i++)
            {
                currentSplitSum += cookieValuesNo[t[i]];
            }

            if (currentSplitSum > bestSum)
            {
                bestSum = currentSplitSum;
            }
        }

        delete[] cookiesCollected;

    }else{
        for(int i=r;i<p;i++)
        {
            t[q]=s[i];
            g(s,p,k,t,q+1,i+1);
        }
    }
}


int main(int argc, char *argv[])
{

    ifstream inputFile(argv[1]);
    ofstream outputFile("output.txt");

    int noTests;

    inputFile>>noTests;

    for (size_t i = 0; i<noTests; i++)
    {
        int noCookies;
        inputFile >> noCookies;
        int* cookieIndexes = new int[noCookies];
        int* tempArray = new int[noCookies];
        cookieValues = new string[noCookies];
        cookieValuesNo = new int[noCookies];

        bestSum = -1;

        for (int j=0; j<noCookies; j++)
        {
            cookieIndexes[j] = j;
            cookieValues[j] = "00000000000000000000";

            int currentCookie;
            inputFile >> currentCookie;
            cookieValuesNo[j] = currentCookie;

            for (int k=MAX_COOKIE_STRING_LENGTH; k>=0; k--)
            {
                int bit = ((currentCookie >> k) & 1);
                if (bit == 0)
                {
                    cookieValues[j][MAX_COOKIE_STRING_LENGTH-k-1] = '0';
                } else {
                    cookieValues[j][MAX_COOKIE_STRING_LENGTH-k-1] = '1';
                }
            }
        }

        // generate subsets and count

//        for (int j=0;j<noCookies; j++)
//        {
//            cout<<cookieValues[j]<<endl;

//        }

        for (int j=1;j<noCookies; j++)
        {
            g(cookieIndexes,noCookies,j,tempArray);
        }

        outputFile<<"Case #"<<i+1<<": ";
        if (bestSum != -1)
        {
            outputFile<<bestSum<<endl;
        } else {
            outputFile<<"NO"<<endl;
        }

        delete[] cookieIndexes;
        delete[] tempArray;
        delete[] cookieValues;
        delete[] cookieValuesNo;

    }
}
