#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>


using namespace std;

long int str2num(string );
typedef vector<string> vecstring_t ;
typedef vector<string>::iterator vecstring_it;
typedef map<int, int> mapint_t ;
typedef map<int, int>::iterator mapint_it;

int count_swap(vecstring_t, vecstring_t, mapint_t);
int findmap(mapint_t, int);

int main(int argc, char* argv[])
{
	ifstream input;
	string line;
	if(argc!=2)
	{
		cout<<"Usage: "<<argv[0]<<" FILENAME"<<endl;
		exit(EXIT_FAILURE);
	}
	input.open(argv[1], ifstream::in);
	if(!input.is_open())
	{
		cerr<<"Error opening file "<<argv[1]<<" !"<<endl;
		exit(EXIT_FAILURE);
	}
	int N;
	getline(input, line);
	N = str2num(line);
	int i,j;
	vecstring_t search, query;
	mapint_t q_index;	
	for(i=0;i<N;i++)
	{
		int s_num;
		int q_num;
		getline(input,line);
		s_num = str2num(line);
		for(j=0;j<s_num;j++)
		{
			getline(input,line);
			search.push_back(line);
		}
		getline(input,line);
		q_num = str2num(line);
		for(j=0;j<q_num;j++)
		{
			getline(input,line);
			query.push_back(line);
			vecstring_it q_it = find(search.begin(),search.end(), line);
			q_index.insert(pair<int,int>(j,q_it-search.begin()));
		
		}
	
		/*
		for(j=0;j<s_num;j++)
		{
			cout<<j<<" - "<<search.at(j)<<endl;
		}
		for(j=0; j<q_num; j++)
		{
			cout<<query.at(j)<<" => "<<"search index = "<<q_index.find(j)->second<<endl;
		}
		*/
			
		int swap = count_swap(search, query, q_index);
		cout<<"Case #"<<i+1<<": "<<swap<<endl;
		
		/* Clear everything	first */
		search.clear();
		query.clear();
		q_index.clear();
	}
	
	input.close();
	return EXIT_SUCCESS;
}

long int str2num(string str)
{
	long int num;
	istringstream Nstr;
	Nstr.str(str);
	Nstr>>num;
	return num;
}

int count_swap(vecstring_t search, vecstring_t query, mapint_t q_index)
{
	int swap = -1;
	int minrest;
	vector<int> rest;
	vector<int>::iterator v_it;
	mapint_it m_it;
	int i;
	int s_num = search.size();
	mapint_t qmap;
	qmap = q_index;
	do
	{
		
		int q_num = query.size();
		for(i=0;i<s_num;i++)
		{
			int first = findmap(qmap,i);
			int cur_rest;
			if(first==-1)
			{
				cur_rest = 0;
			}
			else
				cur_rest = q_num - first;
			rest.push_back(cur_rest);
		}
		v_it = min_element(rest.begin(), rest.end());
		int s_min = v_it - rest.begin();
		minrest = *v_it;
		vecstring_it q_it = find(query.begin(), query.end(), search.at(s_min));
		query.erase(query.begin(), q_it);
		qmap.clear();
		i=0;
		for(q_it=query.begin(); q_it!=query.end(); ++q_it)
		{
			vecstring_it s_it = find(search.begin(), search.end(), *q_it);
			qmap.insert(pair<int, int>(i++, s_it - search.begin()));
		}
		swap++;
		rest.clear();
			
	}while(minrest>0);
	return swap;
}


int findmap(mapint_t qmap, int val)
{
	int index = -1;
	mapint_it it;
	for(it = qmap.begin(); it!=qmap.end(); ++it)
	{
		if(it->second==val)
		{
			index = it->first;
			break;
		}
	}
	return index;
}
//END OF FILE
