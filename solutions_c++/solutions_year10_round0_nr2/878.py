#include <vector>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

bool ge(const char* s, const char* t)
{
    int lenS = strlen(s);
    int lenT = strlen(t);
    if (lenS > lenT)
        return true;
    else if (lenS < lenT)
        return false;
    else
        return strcmp(s, t) >= 0;
}

struct string_less
{
    bool operator() (const string& l, const string& r) const
    {
        return !ge(l.c_str(), r.c_str());
    }
};

bool gt(const char* s, const char* t)
{
    int lenS = strlen(s);
    int lenT = strlen(t);
    if (lenS > lenT)
        return true;
    else if (lenS < lenT)
        return false;
    else
        return strcmp(s, t) > 0;
}

string sub(const char* s, const char* t)
{
    int slen = strlen(s);
    int tlen = strlen(t);
    char* r = new char[slen + 1];
    memset(r, '0', slen);
    r[slen] = '\0';
    const char* ps = s + slen - 1;
    const char* pt = t + tlen - 1;
    char* pr = r + slen - 1;
    bool borrowed = false;
    for (int i = 0; i < tlen; ++i)
    {
        char left = *ps;
        if (borrowed)
        {
            if (*ps >= '1')
            {
                left = *ps - 1;
                borrowed = false;
            }
            else
            {
                left = '9';
                borrowed = true;
            }   
        }
        char right = *pt;
        if (left >= right)
        {
            *pr = '0' + (left - right);
        }
        else
        {
            *pr = '0' + (left + 10 - right);
            borrowed = true;
        }
        ps --;
        pt --;
        pr --;
    }
    for (int i = tlen; i < slen; ++i)
    {
        if (borrowed)
        {
            if (*ps >= '1')
            {
                *pr = *ps - 1;
                borrowed = false;
            }
            else
            {
                *pr = '9';
                borrowed = true;
            }
        }
        else
        {
            *pr = *ps;
        }
        ps --;
        pr --;
    }
    char* seek(r);
    while (*seek == '0')
    {
        seek ++;
    }
    if (*seek == '\0')
    {
        delete []r;
        return "0";
    }
    else
    {
        string tmp = seek;
        delete []r;
        return tmp;
    }
}

string add(const char* s, const char* t)
{
    int slen = strlen(s);
    int tlen = strlen(t);
    int maxLen = slen >= tlen ? slen : tlen;
    int minLen = slen <= tlen ? slen : tlen;
    char* r = new char[maxLen + 2];
    memset(r, '0', maxLen + 1);
    r[maxLen+1] = '\0';
    const char* ps = s + slen - 1;
    const char* pt = t + tlen - 1;
    char* pr = r + maxLen;
    int given = 0;
    for (int i = 0; i < maxLen; ++i)
    {
        int sum = given;
        if (i < slen)
            sum += (*ps - '0');
        if (i < tlen)
            sum += (*pt - '0');
        if (sum >= 10)
        {
            *pr = '0' + (sum - 10);
            given = 1;
        }
        else
        {
            *pr = '0' + sum;
            given = 0;
        }
        ps --;
        pt --;
        pr --;
    }
    if (given > 0)
    {
        *pr = '0' + given;
    }
    char* seek(r);
    while (*seek == '0')
    {
        seek ++;
    }
    if (*seek == '\0')
    {
        delete []r;
        return "0";
    }
    else
    {
        string tmp(seek);
        delete []r;
        return tmp;
    }
}

string calcMaxCommonDivisor(const char* s, const char* t)
{
    string p(s);
    string q(t);
    if (p == "0")
        return q;
    if (q == "0")
        return p;

    while (p != q)
    {
        if (ge(p.c_str(), q.c_str()))
        {
            p = sub(p.c_str(), q.c_str());
        }
        else
        {
            q = sub(q.c_str(), p.c_str());
        }
    }
    return p;
}

void processInput(const char* filePath)
{
    ifstream ifs;
    ifs.open(filePath);
    int T;
    ifs >> T;
    for (int i = 0; i < T; ++i)
    {
        int N;
        ifs >> N;
        vector<string> times(N);
        for (int j = 0; j < N; ++j)
        {
            ifs >> times[j];
        }
        sort(times.rbegin(), times.rend(), string_less());
        string mcd = sub(times[0].c_str(), times[1].c_str()).c_str();
        for (int j = 0; j < N-1; ++j)
        {
            string cha = sub(times[j].c_str(), times[j+1].c_str()).c_str();
            if (cha != "0")
            {
                mcd = calcMaxCommonDivisor(mcd.c_str(), cha.c_str());
            }
        }
        string target = mcd;
        uint64_t start = atoll(times[0].c_str());
        uint64_t end = atoll(target.c_str());
        uint64_t yu = start % end;
        string y;
        if (yu == 0)
        {
            y = "0";
        }
        else
        {
            char news[100];
            sprintf(news, "%lu", end - yu);
            y = news;
        }
        cout << "Case #" << i+1 << ": " << y << endl;
    }
    ifs.close();
}

int main(int argc, char* argv[])
{
    char* filePath = argv[1];
    string s;
    string t;
    processInput(filePath);
}
