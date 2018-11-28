#include <map>
#include <list>
#include <vector>
#include <cstdio>
using namespace std;

class node{
public:
        map<char, node*> token;
        node* parent;
};
class comp_node{
public:
        list<char>::iterator it;
        list<char>::iterator end;
        list<char>::iterator begin;
};
int main(int argc, char* argv[])
{
        int L,D,N;
        node lists;
        char string [500];
        char* string_ptr;
        map<char, node*>::iterator it;
        FILE *fp = fopen(*(argv+1), "r");
        fscanf(fp, "%d %d %d", &L, &D, &N);
        fgets(string, 20, fp);
        for(int i = 0; i < D; i++)
        {
                node *dict_ptr = &lists;
                fgets(string, 20, fp);
                string_ptr = string;
                for(int j =0; j < L; j++)
                {
                        char alphabet = *string_ptr;
                        if( dict_ptr->token.end() == (it = dict_ptr->token.find(alphabet)))
                        {
                                node* temp_ptr = new node;
                                temp_ptr->parent = dict_ptr;
                                dict_ptr->token.insert(pair<char, node*>(alphabet, temp_ptr));
                                dict_ptr = temp_ptr;
                        }
                        else
                        {
                                dict_ptr = it->second;
                        }
                        string_ptr++;
                }
        }
        for(int i = 0; i < N; i++)
        {
                fgets(string, 500, fp);
                string_ptr = string;
                vector<list<char> > string_data(L);
                vector<list<char> >::iterator data_it = string_data.begin();
                vector<comp_node> comp_ptr(L);
                vector<comp_node>::iterator comp_it = comp_ptr.begin();
                for(int j = 0; j < L; j++)
                {
                        char alphabet = *string_ptr;
                        if(alphabet == '(')
                        {
                                string_ptr++;
                                alphabet = *string_ptr;
                                while(')' != alphabet)
                                {
                                        data_it->push_back(alphabet);
                                        string_ptr++;
                                        alphabet = *string_ptr;
                                }
                        }
                        else
                        {
                                data_it->push_back(alphabet);
                        }
                        string_ptr++;
                        comp_it->begin = data_it->begin();
                        comp_it->end = data_it->end();
						comp_it->end--;
                        comp_it->it = data_it->begin();
                        comp_it++;
                        data_it++;
                }
                comp_it = comp_ptr.begin();
                node* dict_ptr = &lists;
                int match = 0;
                while(1)
                {
                        char alphabet = *(comp_it->it);
                        map<char, node*>::iterator iter = dict_ptr->token.find(alphabet);
                        if(iter == dict_ptr->token.end())
                        {
                                if(comp_it->it != comp_it->end)
                                {
                                        (comp_it->it)++;
                                }
                                else
                                {
                                        while(comp_it != comp_ptr.begin() && comp_it->it == comp_it->end)
                                        {
                                                comp_it->it = comp_it->begin;
                                                comp_it--;
                                                dict_ptr = dict_ptr->parent;
                                        }
                                        if(comp_it == comp_ptr.begin() && comp_it->it == comp_it->end)
                                        {
                                                break;
                                        }
                                        (comp_it->it)++;
                                }
                        }
                        else
                        {
                                if(comp_it != (--comp_ptr.end()))
                                {
                                        comp_it++;
                                        dict_ptr = iter->second;
                                }
                                else
                                {
                                        match++;
                                        if(comp_it->it != comp_it->end)
                                        {
                                                (comp_it->it)++;
                                        }
                                        else
                                        {
                                                while(comp_it != comp_ptr.begin() && comp_it->it == comp_it->end)
                                                {
                                                        comp_it->it = comp_it->begin;
                                                        comp_it--;
                                                        dict_ptr = dict_ptr->parent;
                                                }
                                                if(comp_it == comp_ptr.begin() && comp_it->it == comp_it->end)
                                                {
                                                        break;
                                                }
                                                (comp_it->it)++;
                                        }
                                }
                        }
                }
                printf("Case #%d: %d\n", i+1, match);
        }
}
