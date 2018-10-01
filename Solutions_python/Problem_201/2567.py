t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
  n, k = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

  bathroom = [0 for s in range(0, n+2)]
  bathroom[0] = 1
  bathroom[len(bathroom)-1] = 1

  for j in range(0,k):
      empty_stalls = list()
      for s in range(0, n + 2):
        if bathroom[s] == 0:
            Ls = -1
            k = s
            while bathroom[k] != 1:
                Ls += 1
                k -= 1

            Lr = -1
            k = s
            while bathroom[k] != 1:
                Lr += 1
                k += 1

            empty_stalls.append((s,Ls,Lr))

      maximal_min_Ls_Lr = 0
      # maximal_max_Ls_Lr = 0

      potential_fit = list()

      for (s,Ls,Lr) in empty_stalls:
        if min(Ls,Lr) == maximal_min_Ls_Lr:
            potential_fit.append((s,Ls,Lr))
        if min(Ls,Lr) > maximal_min_Ls_Lr:
            maximal_min_Ls_Lr = min(Ls,Lr)
            potential_fit = list()
            potential_fit.append((s, Ls, Lr))
        # if max(Ls, Lr) > maximal_max_Ls_Lr:
        #     maximal_max_Ls_Lr = max(Ls, Lr)


      maximal_max_potential_Ls_Lr = 0
      for (s, Ls, Lr) in potential_fit:
          if max(Ls, Lr) > maximal_max_potential_Ls_Lr:
              maximal_max_potential_Ls_Lr = max(Ls, Lr)


      final_fit = (0,0,0)

      if len(potential_fit) == 1:
          final_fit = potential_fit[0]
      else:
          for (s, Ls, Lr) in potential_fit:
              if max(Ls, Lr) == maximal_max_potential_Ls_Lr:
                  final_fit = (s, Ls, Lr)
                  break

      (s,_,_) = final_fit
      bathroom[s] = 1

  print("Case #" + str(i) + ": " + str(maximal_max_potential_Ls_Lr) + " " + str(maximal_min_Ls_Lr))
