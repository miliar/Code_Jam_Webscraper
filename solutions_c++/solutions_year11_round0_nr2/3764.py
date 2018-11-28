#include <iostream>
#include <string>
using namespace std;

#define COMB_SMALL_INP 1
#define OPPO_SMALL_INP 1
#define LIST_SMALL_INP 10

#define COMB_LARGE_INP 36
#define OPPO_LARGE_INP 28
#define LIST_LARGE_INP 100

#define BASE_ELEMENT_SIZE 8

struct comb_info
{
	char ch[4]; //base, other, nonbase
	int id_chk;
	int id_found;
	comb_info(): id_chk(-1), id_found(-1)
	{
		ch[0]=ch[1]=ch[2]=ch[3]='\0';
	}
};

struct opp_info
{
	char ch[3];
	int id_chk;
	opp_info():id_chk(-1)
	{
		ch[0]=ch[1]=ch[2]='\0';
	}
};



int main()
{
	int test_num=0;
	cin >> test_num;
	
	std::string outputStr;

	int it_test;
	for(it_test=0; it_test < test_num; it_test++)
	{
		int comb_num = 0;
		cin >> comb_num;
		
		
		comb_info *ptr_combinfo = NULL;
		if(comb_num > 0) ptr_combinfo = new comb_info[comb_num];

		//read comb;
		int it_comb;
		for( it_comb=0; it_comb < comb_num; it_comb++)
		{
			cin >> ptr_combinfo[it_comb].ch[0];
			cin >> ptr_combinfo[it_comb].ch[1];
			cin >> ptr_combinfo[it_comb].ch[2];
		}

		int opp_num = 0;
		cin >> opp_num;
		
		opp_info *ptr_oppinfo = NULL;
		if(opp_num > 0) ptr_oppinfo = new opp_info[opp_num];

		//read comb;
		int it_opp;
		for( it_opp=0; it_opp< opp_num; it_opp++)
		{
			cin >> ptr_oppinfo[it_opp].ch[0];
			cin >> ptr_oppinfo[it_opp].ch[1];
		}

		// read invok list
		int invoke_num = 0;
		cin >> invoke_num;
		
		char invoke_elem_list[LIST_SMALL_INP]={'\0'};
		if( invoke_num > LIST_SMALL_INP )
		{
			invoke_num = LIST_SMALL_INP;
			cout << "Warning can only read upto " << LIST_SMALL_INP << " invokations" << endl;
		}

		comb_info *combfound = NULL;
		opp_info *oppfound[LIST_SMALL_INP];
		for( int it = 0; it < LIST_SMALL_INP; it++)
			oppfound[it] = NULL;
		int invoke_list_start_id = 0;

		int it_invoke;
		for( it_invoke = 0; it_invoke < invoke_num; it_invoke++)
		{
			cin >> invoke_elem_list[it_invoke];
			bool skip_full_chk = false;
			if( combfound != NULL )
			{
				if( combfound->ch[ combfound->id_chk ] == invoke_elem_list[it_invoke] )
				{
					invoke_elem_list[it_invoke]='\0';
					invoke_elem_list[it_invoke-1]=combfound->ch[2]; // Add non-base
					oppfound[it_invoke]=oppfound[it_invoke-1]=NULL;
					skip_full_chk = true;
					combfound = NULL;
				}
				else if ( combfound->ch[ combfound->id_found] == invoke_elem_list[it_invoke])
					skip_full_chk = true;
				else
					combfound = NULL;
			}
			if( skip_full_chk && combfound==NULL) continue;

			int it_opp_info;
			for (it_opp_info=invoke_list_start_id; it_opp_info < it_invoke; it_opp_info++)
			{
				opp_info *op_inf = oppfound[it_opp_info];
				if( op_inf == NULL)
					continue;
				
				if( op_inf->ch[op_inf->id_chk] == invoke_elem_list[it_invoke])
				{
					for( int it = invoke_list_start_id; it <= it_invoke; it++)
					{
						invoke_elem_list[it]='\0';
						oppfound[it_opp_info]= NULL;
					}
					invoke_list_start_id = it_invoke+1; 
					skip_full_chk = true;
				}
			}
			if(skip_full_chk)
				continue;

			// Full chk
			bool found_c = false;
			for( it_comb=0; it_comb < comb_num; it_comb++)
			{
				if( ptr_combinfo[it_comb].ch[0] == invoke_elem_list[it_invoke])
				{
					found_c = true;
					ptr_combinfo[it_comb].id_chk = 1;
					ptr_combinfo[it_comb].id_found = 0;
				}
				else if( ptr_combinfo[it_comb].ch[1] == invoke_elem_list[it_invoke])
				{
					found_c = true;
					ptr_combinfo[it_comb].id_chk = 0;
					ptr_combinfo[it_comb].id_found = 1;
				}
				if(found_c)
				{
					combfound = &ptr_combinfo[it_comb];
					break;
				}
			}
			
			bool found_o = false;
			for( it_opp=0; it_opp < opp_num; it_opp++)
			{
				if( ptr_oppinfo[it_opp].ch[0] == invoke_elem_list[it_invoke])
				{
					found_o = true;
					ptr_oppinfo[it_opp].id_chk = 1;
				}
				else if( ptr_oppinfo[it_opp].ch[1] == invoke_elem_list[it_invoke])
				{
					found_o = true;
					ptr_oppinfo[it_opp].id_chk = 0;
				}

				if( found_o )
				{
					oppfound[it_invoke] = &ptr_oppinfo[it_opp];
					break;
				}				
			}

		}
		
		if(ptr_oppinfo)
			delete [] ptr_oppinfo;
		ptr_oppinfo = NULL;
		if(ptr_combinfo)
			delete [] ptr_combinfo;
		ptr_combinfo= NULL;

		//cout << "Case #" << it_test+1 << ": " << global_time << endl;
		
		// temp
		char outp[100];
		sprintf( outp, "Case #%d: [", it_test+1);
		outputStr+= outp;

		bool empty_list = true;
		for( int it = invoke_list_start_id; it < invoke_num; it++)
		{
			if(invoke_elem_list[it] != '\0' )
			{empty_list = false;
				if(it != invoke_list_start_id)
					outputStr+= ", ";
				outputStr+= invoke_elem_list[it];
			}
		}
		if(empty_list) outputStr+= "";
		outputStr+= "]\n";
	}
	//std::cout << "Hellow " << std::endl;
	cout << "Output " << endl << endl;
	cout << outputStr;
	return 0;
}

//struct Base_element_info
//{
//	char elem;
//	const Base_element_info *comb_inf[BASE_ELEMENT_SIZE];
//	const Base_element_info *oppo_inf[BASE_ELEMENT_SIZE];
//	char comb_non_base[BASE_ELEMENT_SIZE];
//
//	Base_element_info(char el): elem(el)
//	{
//		reset();
//	}
//	void reset()
//	{
//		for( int it = 0; it < BASE_ELEMENT_SIZE; it++)
//		{
//			comb_inf = null;
//			oppo_inf = null;
//			comb_non_base='\0';
//		}
//	}
//};
//
//struct Base_elem_info_list
//{
//	Base_element_info base_elem_inf[BASE_ELEMENT_SIZE];
//	Base_elem_info_list()
//	{
//		if( BASE_ELEMENT_SIZE != 8) cout << "Problem!!!" << endl;
//
//		base_elem_inf[0].elem='Q';
//		base_elem_inf[1].elem='W';
//		base_elem_inf[2].elem='E';
//		base_elem_inf[3].elem='R';
//		base_elem_inf[4].elem='A';
//		base_elem_inf[5].elem='S';
//		base_elem_inf[6].elem='D';
//		base_elem_inf[7].elem='F';
//	}
//
//	int find_index( char ch )
//	{
//		switch(base)
//		{
//		case 'Q':
//			return 0;			
//		case 'W':
//			return 1;
//		case 'E':
//			return 2;
//		case 'R':
//			return 3;
//		case 'A':
//			return 4;
//		case 'S':
//			return 5;
//		case 'D':
//			return 6;
//		case 'F':
//			return 7;
//		default:
//			cout << "Problem!!!" << endl;
//		}
//		return -1;
//	}
//
//	void add_comb_info(char base, char other, char non_base )
//	{
//		int id_base = find_index(base);
//		int id_other = find_index(other);
//		
//		if( id_base == -1 || id_other == -1) return;
//		
//		base_elem_inf[id_base].comb_inf[id_other]=base_elem_inf[id_other];
//		base_elem_inf[id_other].comb_inf[id_base]=base_elem_inf[id_base];
//		base_elem_inf[id_base].comb_non_base = non_base;
//	}
//};