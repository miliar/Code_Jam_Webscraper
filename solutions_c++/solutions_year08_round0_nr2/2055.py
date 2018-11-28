#include <iostream>
#include <conio.h>

typedef struct linked_list* ll;

FILE *fp;
    
struct linked_list 
{
        int value; 
        ll next;
        };

ll a_dept, a_arrv, b_dept, b_arrv;

enum station
{
     st_a = 0,
     st_b
 };
 
 enum wh_time
 {
      dept = 0,
      arrv
  };

int a_count, b_count;

void ll_print (int st, int wh) {
ll lst;
     switch (st)
     {
            case st_a:
                 switch (wh)
                 {
                        case dept:
                             lst = a_dept;
                             break;
                        case arrv:
                             lst = a_arrv;
                             break;
                        }
                 break;
            case st_b:
                 switch (wh)
                 {
                        case dept:
                             lst = b_dept;
                             break;
                        case arrv:
                             lst = b_arrv;
                             break;
                        }
                 break;
            
            }
 printf ("\n\nPRINTING %d %d\n\n", st, wh);
 while(lst != NULL) {
  printf("%d\n", lst->value);
  lst = lst->next;
 }

}


void push (int st, int wh, int time)
{
     ll tmp,lst,prev;
     tmp = (ll) malloc (sizeof(struct linked_list));
     tmp->value = time;
     tmp->next = NULL;
     switch (st)
     {
            case st_a:
                 switch (wh)
                 {
                        case dept:
                             if (NULL == a_dept)
                             {
                                      a_dept = tmp;
                                return;
                             }
                             lst = a_dept;
                             break;
                        case arrv:
                             if (NULL == a_arrv)
                             {
                                      a_arrv = tmp;
                                return;
                             }
                             lst = a_arrv;
                             break;
                        }
                 break;
            case st_b:
                 switch (wh)
                 {
                        case dept:
                             if (NULL == b_dept)
                             {
                                      b_dept = tmp;
                                return;
                             }
                             lst = b_dept;
                             break;
                        case arrv:
                             if (NULL == b_arrv)
                             {
                                      b_arrv = tmp;
                                return;
                             }
                             lst = b_arrv;
                             break;
                        }
                 break;
            
            }
     

     if (tmp->value < lst->value)    
     {
                    tmp->next = lst;
                    
       switch (st)
     {
            case st_a:
                 switch (wh)
                 {
                        case dept:
                             a_dept = tmp;
                             break;
                        case arrv:
                             a_arrv = tmp;
                             break;
                        }
                 break;
            case st_b:
                 switch (wh)
                 {
                        case dept:
                             b_dept = tmp;
                             break;
                        case arrv:
                             b_arrv = tmp;
                             break;
                        }
                 break;
            
            }                  
                    
                    return;
                    }
     prev = lst;
     lst = lst->next;
     while (lst) 
     {      
     if (tmp->value < lst-> value)
     {
                    tmp->next = prev->next;
                    prev->next = tmp;
                    return;
                    }
                    prev = lst;
                    lst = lst->next;
                    }
                    
     prev->next = tmp;
 }

void input_ll()
{
     int temp_hr, temp_min, temp_time;
    fscanf (fp,"%d %d", &a_count, &b_count);
//    printf ("%d %d\n", a_count, b_count);
    
    for (int i=0; i< a_count; i++)
    {
       fscanf (fp,"%d:%d", &temp_hr, &temp_min);
       temp_time = 60* temp_hr + temp_min;
       push (st_a, dept, temp_time);
       fscanf (fp,"%d:%d", &temp_hr, &temp_min);
       temp_time = 60* temp_hr + temp_min;
       push (st_a, arrv, temp_time);
    }
    
    for (int i=0; i< b_count; i++)
    {
       fscanf (fp,"%d:%d", &temp_hr, &temp_min);
       temp_time = 60* temp_hr + temp_min;
       push (st_b, dept, temp_time);
       fscanf (fp,"%d:%d", &temp_hr, &temp_min);
       temp_time = 60* temp_hr + temp_min;
       push (st_b, arrv, temp_time);
    }    
    
          }

int turnaround;
void optimize()
{
     ll tmp_dept, tmp_arrv;
     
     tmp_dept = a_dept;
     tmp_arrv = b_arrv;
     
     while (tmp_dept && tmp_arrv)
     {
           if (tmp_dept->value >= tmp_arrv->value + turnaround)
           {
                               a_count--;
                               tmp_arrv = tmp_arrv->next;
                               }
                               tmp_dept = tmp_dept->next;
           }
           
     tmp_dept = b_dept;
     tmp_arrv = a_arrv;
     
     while (tmp_dept && tmp_arrv)
     {
           if (tmp_dept->value >= tmp_arrv->value + turnaround)
           {
                               b_count--;
                               tmp_arrv = tmp_arrv->next;
                               }
                               tmp_dept = tmp_dept->next;
           }           
 }

int main()
{
    int Cases;
    int i;
    FILE *fout;

    if ( NULL == (fp = fopen ("input.txt", "r")) )
    {
	printf (" Error opening input file\n");
	exit (1);
    }
   
    fseek (fp, 0, 0);
    fscanf (fp, "%d", &Cases);
    printf ("Cases = %d\n", Cases);

    if ( NULL == (fout = fopen ("out.txt", "w")) )
    {
	printf (" Error opening input file\n");
	exit (1);
    }    
    
    /*We run all steps for each case*/
    for ( i = 0; i < Cases; i++)
    {
        a_dept = NULL;
        a_arrv = NULL;
        b_dept = NULL;
        b_arrv = NULL;
    fscanf (fp,"%d", &turnaround);
//	printf ("Turn Around = %d\n", turnaround);
	input_ll();
//	ll_print (0,0);
//	ll_print (0,1);
//	ll_print (1,0);
//	ll_print (1,1);	
	
	optimize();
 //   ll_print (1,1);	
	fprintf (fout,"Case #%d: %d %d\n",i+1, a_count, b_count);
}
fclose (fout);
 }
