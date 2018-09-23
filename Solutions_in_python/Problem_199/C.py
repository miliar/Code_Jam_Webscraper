for t in range(int(input())):
 stack, k = input().split()
 stack=list(stack)
 k=int(k)
 c=0
 for i in range(len(stack)-k+1):
  if stack[i]=='-':
   for j in range(i, i+k):
    stack[j] = "+" if stack[j]=="-" else "-"
   c+=1
 print("Case #{t}: {a}".format(t=t+1, a=c if "-" not in stack else "IMPOSSIBLE"))
