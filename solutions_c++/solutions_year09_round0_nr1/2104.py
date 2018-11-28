#include<iostream>
#include<string>
#include<vector>
#include<map>

using namespace std;

class CLetter
{
    private:
        map<char, CLetter> nextLetter;
        map<char, CLetter>::iterator it;
    public:
        void add(char *str);
        int count(char *pat);
        void write();
};

void CLetter::add(char *str)
{
    CLetter *nextEntry;
    if(nextLetter.find(*str)==nextLetter.end())
    {
        nextEntry=new CLetter();
        nextLetter[*str]=*nextEntry;
    }

    if(*str!='\0')
        nextLetter[*str].add(str+1);
}

void CLetter::write()
{
    cout << "(";
    for(it=nextLetter.begin();it!=nextLetter.end();++it)
    {
        if(it->first!='\0')
            cout << it->first;
        else
            cout << ".";
        it->second.write();
    }
    cout << ")";
}

int CLetter::count(char *pat)
{
    char *e;

    int count=0,t=0;
    if(!*pat)
        return 1;

    if(*pat=='(')
    {
        ++pat;
        for(e=pat;*e!=')';++e,++t);
        ++e;

        for(;*pat!=')';++pat)
            if((it=nextLetter.find(*pat))!=nextLetter.end())
                count+=it->second.count(e);

    } else
    {
        if((it=nextLetter.find(*pat))!=nextLetter.end())
            return it->second.count(pat+1);
    }

    return count;
}

int main()
{
	int tot, cn, caseCount=0, L, D;
	int i;
	string s;
	char *word;
	CLetter dic;

	cin >> L >> D >> tot;
	word=new char[L+1];

	//Build dictionary
	for(i=0;i<D;++i)
	{
	    cin >> word;
	    word[L]='\0';
	    dic.add(word);
	}
	//dic.write();cout << endl;

	//Process words
	for(cn=0;cn<tot;++cn)
	{
	    //i/p & process
	    cin >> s;

	    word=(char *)s.c_str();
	    //o/p
	    cout << "Case #" << ++caseCount << ": ";
        cout << dic.count(word);;
	    cout << endl;
	}
	return 0;
}
