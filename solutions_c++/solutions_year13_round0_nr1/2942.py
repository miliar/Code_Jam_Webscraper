#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

int result(string v)
{
    bool X = false;
    bool O = false;
    bool d = false;
    bool T = false;
    for (int i = 0; i < 4; ++i)
    {
	switch(v[i])
	{
	    case 'X': X = true; break;
	    case 'O': O = true; break;
	    case '.': d = true; break;
	    case 'T': T = true; break;
	}
	
    }

    if ( X && O || d)
	return 0; // non meaningful
    else if (X)
	return 1; // x wins
    else return -1; // y wins
}

int main(int argc, char *argv[])
{
    if (argc!=3) 
    {
	cout << "Missing arguments." << endl;
	return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int num;
    fin >> num;
    vector<vector<vector<char> > > v;
    v.resize(num);
    for (int i = 0; i < num; ++i)
    {
	v[i].resize(4);

	for (int j = 0; j < 4; ++j)
	    v[i][j].resize(4);
    }
    string s;
    for (int i = 0; i < num; ++i)
    {
	for (int j = 0; j < 4; ++j)
	{
	    
	    fin >> s;
	    for (int k = 0; k < 4; ++k)
	    {
		v[i][j][k] =s[k];
	    }
	}
    }

    for (int i = 0; i < num; ++i)
    {
	int flag = 0;
	string u, w;
	for (int j = 0; j < 4; ++j)
	{
	    string s, t;
	    for (int k = 0; k < 4; ++k)
	    {
		s.push_back(v[i][j][k]);
		t.push_back(v[i][k][j]);
		u.push_back(v[i][k][k]);
		w.push_back(v[i][k][3-k]);
	    }
	    flag = result(s);
	    if (flag!=0) break;
	    flag = result(t);
	    if (flag!=0) break;
	    flag = result(u);
	    if (flag!=0) break;
	    flag = result(w);
	    if (flag!=0) break;

	}    
	fout << "Case #" << i+1 << ": ";
	if (flag == 1)
	    fout << "X won" << endl;
	else if(flag ==-1)
	    fout << "O won" << endl;
	else
	{
	    bool draw = true;
	    for (int j= 0; j < 4; ++j)
		for (int k= 0; k < 4; ++k)
		    if (v[i][j][k]=='.') draw = false;

	    if (draw)
		fout << "Draw" << endl;
	    else 
		fout << "Game has not completed"<< endl;
	}
    }
    return 0;
}
