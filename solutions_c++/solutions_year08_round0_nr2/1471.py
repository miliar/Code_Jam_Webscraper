#include<iostream>
using namespace std;

struct line{
       int starth,startm;
       int finishh,finishm;
       bool usecar;
       };
void sort(line array[100],int start,int finish)
{
     int mid=start+(finish-start)/2;
     line *tmp=new line[100];
     if(finish>(start+1))
        {
            
            sort(array,start,mid);  
            sort(array,mid,finish);
            //cout << "haha";
        }
     
       
            
            int index1=start;
            int index2=mid;
            int index=0;
            while(index1!=mid && index2!=finish)
            {
                 if((array[index1].starth*60+array[index1].startm)>(array[index2].starth*60+array[index2].startm))       
                 {
                      tmp[index]=array[index2];
                      index++;index2++;
                      //cout << array[index2].starth<<" ";
                      }
                 else
                 {
                     tmp[index]=array[index1];
                     index++;index1++;
                 }
            }
            while(index2==finish && index1!=mid){tmp[index]=array[index1];index++;index1++;}
            while(index1==mid && index2!=finish){tmp[index]=array[index2];index++;index2++;}
       
       for(int i=0;i<(finish-start);i++)
       {
               array[i+start]=tmp[i];
               //cout << array[i].starth <<" " << tmp[i].starth<<endl;
       }
}


int main()
{
    int haha;
    cin >> haha;
    for(int k=0;k<haha;k++)
    {
    
    int wait;
    cin >> wait;
    int ftosn,stofn;
    line ftos[100];
    line stof[100];
    
    cin >>ftosn >> stofn;
    
    for(int i=0;i<ftosn;i++)
    {
            char temp[50];
            cin >> temp;
            char* hour;
            hour=strtok(temp,":");
            char* minute= strtok(NULL,":");
            ftos[i].starth=atoi(hour);
            ftos[i].startm=atoi(minute);
            ftos[i].usecar=1;
            //cout << ftos[i].starth<<" "<< ftos[i].startm<< endl;
            
            cin >> temp;
            //char* hour;
            hour=strtok(temp,":");
            minute= strtok(NULL,":");
            ftos[i].finishh=atoi(hour);
            ftos[i].finishm=atoi(minute);
            //cout << ftos[i].finishh<<" "<< ftos[i].finishm<< endl;         
    }       
    
    for(int i=0;i<stofn;i++)
    {
            char temp[50];
            cin >> temp;
            char* hour;
            hour=strtok(temp,":");
            char* minute= strtok(NULL,":");
            stof[i].starth=atoi(hour);
            stof[i].startm=atoi(minute);
            stof[i].usecar=1;
            //cout <<
            
            cin >> temp;
            //char* hour;
            hour=strtok(temp,":");
            minute= strtok(NULL,":");
            stof[i].finishh=atoi(hour);
            stof[i].finishm=atoi(minute);
            //cout << 
    }      
    //cout << ftosn <<endl;
    sort(ftos,0,ftosn);
    /*for(int i=0;i<ftosn;i++)
       cout <<  ftos[i].starth<<" "<< ftos[i].startm<< endl;*/
    sort(stof,0,stofn);
    /*cout <<endl;
    cout << stofn <<endl;
    for(int i=0;i<stofn;i++)
       cout << stof[i].starth<<" "<< stof[i].startm<< endl;*/
    for(int i=0;i<ftosn;i++)
    {
            for(int j=0;j<stofn;j++)
            {
                if((stof[j].starth*60+stof[j].startm-wait)>=(ftos[i].finishh*60+ftos[i].finishm) && stof[j].usecar==1)
                {
                        stof[j].usecar=0;
                        break;
                }
            }
    }
    for(int i=0;i<stofn;i++)
    {
            for(int j=0;j<ftosn;j++)
            {
                if((ftos[j].starth*60+ftos[j].startm-wait)>=(stof[i].finishh*60+stof[i].finishm) && ftos[j].usecar==1)
                {
                        ftos[j].usecar=0;
                        break;
                }
            }
    }
    
    int count=0;
    cout << "Case #" << k+1 << ": ";
    for(int i=0;i<ftosn;i++)
    {
            if(ftos[i].usecar){count++;}
    }
    cout <<count << " ";
    
    count=0;
    for(int i=0;i<stofn;i++)
    {
            if(stof[i].usecar){count++;}
    }
    //cout << stofn;
    cout <<count<<endl;
    }
    //system("pause");
    return 0;
}