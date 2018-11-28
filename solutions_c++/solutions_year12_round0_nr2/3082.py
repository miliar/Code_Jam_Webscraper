#include "Common.h"

void main()
{
	FileIO		file;
	Display		dis;
	Tokenizer	tok;
	strarr		arr;
	strarr		out;
	file.read(arr, "B-large.in");
	//dis.show(arr);
	for(string::size_type i=1 ; i<arr.size() ; i++)
	{
		string &line = arr.at(i);
		strarr token;
		tok.tokenize(token, line);
		token.at(0);
		int sur = atoi(token.at(1).c_str());
		int min = atoi(token.at(2).c_str());
		token.erase(token.begin());
		token.erase(token.begin());
		token.erase(token.begin());
		vector<int> token_i;
		for(int s=0 ; s<token.size() ; s++)
		{	token_i.push_back(atoi(token[s].c_str()));}
		token.empty();
		sort(token_i.begin(), token_i.end());   
		reverse(token_i.begin(),token_i.end());
		int max_no=0;
		for(int s=0 ; s<token_i.size() ; s++)
		{
			int score = token_i.at(s);
			if(score >= min +
				(crop<int>((min-1),0)<<1))//inisde limits of min
			{}
			else
			{
				if(sur <= 0)//if surprising result over
				{	continue;}
				if(score >= min +
					(crop<int>((min-2),0)<<1))//the least possible, with best res eq min
				{	sur--;}
				else//best result smaller the min
				{	continue;}
			}
			max_no++;
		}
		string	res("Case #");
		char	buf[16];
		res.append(_itoa(i,buf,10));
		res.append(": ");
		res.append(_itoa(max_no,buf,10));
		out.push_back(res);
	}
	dis.show(out);
	//dis.show(outline);
	file.write(out);
	getch();
}