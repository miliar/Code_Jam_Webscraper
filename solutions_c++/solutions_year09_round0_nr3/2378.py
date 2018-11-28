// *** Note: This program uses a trick to synchronize cin>> & cin.getline() - eating up the extra CR/LF after N using a call to cin.get()   [line 75]                             ***
// ***       If that causes any input-related problems (typically the first input would be blank, and the last one skipped), then uncomment the following to try an alternative:  ***
//#define CINSYNC

#include<iostream>
#include<iomanip>
//#include<stdio.h>
#include<string>

#define MAXLEN 500 // small: 30; large: 500
#define MODULUS 10000

using namespace std;

//const int theLength = 19;
//const char theString[theLength+1] = "welcome to code jam";
//char input[MAXLEN+1];

string theString("welcome to code jam");
int strLength;
char inpBuff[MAXLEN+1];
string input;
int inpLength;

int rec_letter(int posStr, int posInput);
int rec_occurrence(int posStr, int posInput);

int rec_letter(int posStr, int posInput)
{
    if(posStr >= strLength)
        return 1;

    char myLetter = theString[posStr];

    //cout<<"rec_letter(): "<<myLetter<<endl;

    int myPos = input.find_first_of(myLetter, posInput);

    if(myPos == string::npos)
        return 0;
    else
        return rec_occurrence(posStr, myPos);
}

int rec_occurrence(int posStr, int posInput)
{
    if(posInput >= inpLength)
        return 0;
    else
    {
        int myTotal = 0;
        char myLetter = theString[posStr];
        int myPos=posInput;
        myPos = input.find_first_of(myLetter, myPos);
        while(myPos != string::npos)
        {
            myTotal+=rec_letter(posStr+1, myPos+1);
            if(myTotal > MODULUS)
                myTotal %= MODULUS;

            myPos = input.find_first_of(myLetter, myPos+1);
        }
        return myTotal;
    }
}

int main(int argc, char *argv[])
{
    int N, total;
    
    cin>>N;
#ifdef CINSYNC
    cin.sync();
#else
    cin.get();
#endif
    //scanf("%d", &N);

    cout<<setfill('0');

    for(int mycase=1; mycase<=N; mycase++)
    {
        input.clear();
        input.reserve(MAXLEN+1);
        cin.getline(inpBuff, MAXLEN);
        input = inpBuff;
        //fgets(input, MAXLEN, stdin);

        //cout<<input<<endl;

        strLength = theString.length();
        inpLength = input.length();

        total = rec_letter(0, 0);
        
        cout<<"Case #"<<mycase<<": "<<setw(4)<<total%MODULUS<<endl;
    }

    //system("pause");
    return 0;
}