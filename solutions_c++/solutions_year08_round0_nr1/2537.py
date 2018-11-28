
#include<iomanip>
#include<iostream>
#include<fstream>
#include<cstring>
#include <string>

using namespace std;

struct list        //STORE UNIQUE ENGINE NO
{
    string name;
    short eng_no;
    short freq;
};

struct count
{
    short eng_no;
    short freq;
};

ifstream infile("test.txt");
ofstream outfile("output.txt");

/****************PROTOTYPE******************************/
void input_eginie(list *eg_list, short eg_size);
void input_data(string *data_array, short data_size);
short cacl(list *eg_list, string *data_array, short eg_size, short data_size);
/****************MAIN**********************************/

void main()
{
    char filename[130];
    string array_tmp[1000], str_size_eg, str_size_data, str_size_case;
    string *data_array = array_tmp;
    short eg_size=0, case_size=0, data_size=0, cur_case=0, change=0;                //size record the egine size
    

    //cout<<endl<<"please input the filename."<<endl;
    //cin>>filename;            //input the initial filename from keyboard
    //infile = ifstream (filename);
    //infile >> case_size;
    getline(infile,str_size_case);
    case_size = atoi(str_size_case.c_str());
    for(cur_case=0;cur_case<case_size;cur_case++)
    {
        //infile >> eg_size;
        getline(infile, str_size_eg);
        eg_size = atoi(str_size_eg.c_str());
        list *eg_list = new list [eg_size];
        input_eginie(eg_list, eg_size);
        //infile >> data_size;
        getline(infile,str_size_data);
        data_size= atoi(str_size_data.c_str());

        input_data(data_array, data_size);
        change = cacl(eg_list,data_array, eg_size, data_size);
        cout<<"case"<<cur_case<<": "<<change<<"\n";
        outfile<<"Case #"<<cur_case+1<<": "<<change<<"\n";
    }
    system("pause");
}

/*****************SUB FUNCTION*************************/
void input_eginie(list *eg_list, short eg_size)
{
    short i;
    string tmp;
    list *ptr=eg_list;

    for(i=0;i<eg_size;i++)
    {
        //ptr->name = new char [100];
        //infile >> ptr->name ;
        getline(infile, tmp);
        ptr->name = tmp;
        //strcpy(ptr->name , tmp);
        ptr->eng_no=i;
        ptr->freq=0;
        ptr++;

    }
}

void input_data(string *data_array, short data_size)
{
    short i;

    //data_array = new short [data_size];
    string *sptr = data_array;

     for(i=0;i<data_size;i++)
    {
        
        //infile >> *sptr;
        getline(infile, *sptr);
        sptr++;

    }
}

short cacl(list *eg_list, string *data_array,short eg_size, short data_size)
{
    short switch_no=0, rest_count=0;

    //case 1 
    if (eg_size > data_size)
        return switch_no;
    
    string *d_start = data_array, *d_end = data_array+data_size;
    short i, count_size=0, rest=0;
    list *ptr = eg_list, *j, *k;
    count *result = new count [eg_size];
    count *temp = result ;   

    while(d_start<d_end)
    {
        ptr = eg_list;
        for(i=0;i<eg_size;i++)
        {
            //if(strcmp(ptr->name,d_start)==0)
            if(ptr->name.compare(*d_start) == 0)
            {
				if (ptr->freq == 0)
                {
                    temp->eng_no = ptr->eng_no;

                
                    count_size++;
                    //case 2
                    if (count_size==eg_size) // need to switch now
                    {
                        rest = data_size-rest_count;
                        if(rest<eg_size)
                            return switch_no;
                        switch_no++;
                        count_size=1;
                        result->eng_no = ptr->eng_no;
                        //clean the freq in eg_list
                        j = eg_list;
                        k = eg_list + eg_size;
                        while(j<k)
                        {
                            j->freq = 0;
                            j++;
                        }
                        ptr->freq = 1;
                        break;
                    }
                }
                ptr->freq ++;
               
            }
            ptr++;
        }
        d_start++;
        
    }

    return switch_no;
}
                



            

    


