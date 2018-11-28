#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	int L, D, N;
	ifstream from("A-large.in");
	string input;
 	getline(from, input);
	
	istringstream ist(input);
	ist >> L >> D >> N;
		
	typedef string WORD;
	typedef string::iterator WORD_ITER;

	typedef vector<WORD> VOCAB;
	typedef vector<WORD>::iterator VOCAB_ITER;

	WORD word;
	VOCAB vocab;
	VOCAB check;

	for(int idx=0; idx<D; idx++)
	{
		input.clear();
		getline(from, input);
		vocab.push_back(input);
	}

	for(int idx=0; idx<L; idx++)
	{
		WORD pot;
		for(VOCAB_ITER vocab_iter = vocab.begin(); vocab_iter!=vocab.end(); ++vocab_iter)
		{
			pot+=(*vocab_iter)[idx];
		}
		check.push_back(pot);
	}

	typedef vector<VOCAB> EXPR;
	typedef vector<VOCAB>::iterator EXPR_ITER;

	EXPR expr;
	enum STATE {SINGLE, CLUSTER};

	for(int idx=0; idx<N; idx++)
	{
		STATE state=SINGLE;
		input.clear();
		getline(from, input);

		VOCAB reg;
		WORD part;

		for(string::iterator iter=input.begin(); iter!=input.end(); iter++)
		{
			switch(*iter)
			{
			case '(':
				state=CLUSTER;
				part.clear();
				break;
			case ')':
				reg.push_back(part);
				state=SINGLE;
				part.clear();
				break;
			default:
				if(state==SINGLE)
				{
					reg.push_back(WORD(1,*iter));
				}
				else
				{
					part += *iter;
				}
			}
		}
		expr.push_back(reg);
	}

	vector<int> counter;
	
	for(int idx = 0; idx < N; idx++)
	{
		int count = 0;
		for(VOCAB_ITER vocab_iter = vocab.begin(); vocab_iter != vocab.end(); ++vocab_iter)
		{
			VOCAB_ITER expr_vocab_iter = expr[idx].begin();
			bool todo=true;
			for(WORD_ITER word_iter = vocab_iter->begin(); word_iter!=vocab_iter->end(); ++word_iter, ++expr_vocab_iter)
			{
				if(!(todo &= (find(expr_vocab_iter->begin(), expr_vocab_iter->end(), *word_iter) != expr_vocab_iter->end())))
					break;
			}
			count+= (todo? 1:0);
		}
		counter.push_back(count);
	}

	ofstream to("Out.txt");
	for(size_t idx=0; idx<counter.size(); idx++)
	{
		ostringstream ost;
		ost<<"Case "<<"#"<<idx+1<<": "<<counter[idx];
		to<<ost.str()<<endl;
	}
	from.close();
	to.close();
}
