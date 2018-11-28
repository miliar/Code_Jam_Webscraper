#include<iostream>
    using namespace std;

int main()
{
    int t,j,i,c,d,n,destl,combl,combined,destructed,nnew,k,l;
    char com[36][3],des[28][2],seq[100],comb[8][2],dest[8],seqn[100];
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>c;
        for(j=0;j<c;j++)
        {
            cin>>com[j][0]>>com[j][1]>>com[j][2];
        }
        cin>>d;
        for(j=0;j<d;j++)
        {
            cin>>des[j][0]>>des[j][1];
        }
        cin>>n;
        for(j=0;j<n;j++)
        {
            cin>>seq[j];
        }
        //Start processing
        nnew=0;
        destl=0;
        combl=0;
        //clear comb & desd
        for(j=0;j<n;j++)
        {
            //combining
            //incorporate the removal of the element from dest
            combined=0;
            for(k=0;k<combl;k++)
            {
                if(comb[k][0]==seq[j])
                {
                    combined=1;
                    for(l=0;l<d;l++)
                    {
                        if(des[l][0]==dest[destl-1])
                        {
                            if(des[l][1]==seqn[nnew-1])
                                destl--;
                        }
                        if(des[l][1]==dest[destl-1])
                        {
                            if(des[l][0]==seqn[nnew-1])
                                destl--;
                        }
                    }
                    seqn[nnew-1]=comb[k][1];
                    combl=0;
                    break;
                }
            }
            //destruction
            destructed=0;
            if(combined==0)
            {
                for(k=0;k<destl;k++)
                {
                    if(dest[k]==seq[j])
                    {
                        destructed=1;
                        nnew=0;
                        destl=0;
                        combl=0;
                        break;
                    }
                }
            }
            //normal
            if(combined==0 && destructed==0)
            {
                seqn[nnew++]=seq[j];
                combl=0;
                for(k=0;k<c;k++)
                {
                    if(com[k][0]==seq[j])
                    {
                        comb[combl][0]=com[k][1];
                        comb[combl++][1]=com[k][2];
                    }
                    else if(com[k][1]==seq[j])
                    {
                        comb[combl][0]=com[k][0];
                        comb[combl++][1]=com[k][2];
                    }
                }
                for(k=0;k<d;k++)
                {
                    if(des[k][0]==seq[j])
                        dest[destl++]=des[k][1];
                    else if(des[k][1]==seq[j])
                        dest[destl++]=des[k][0];
                }
            }
        }
        cout<<"Case #"<<i+1<<": [";
        for(j=0;j<nnew;j++)
        {
            if(j!=nnew-1)
                cout<<seqn[j]<<", ";
            else
                cout<<seqn[j];
        }
        cout<<"]\n";
    }
    return 0;
}
